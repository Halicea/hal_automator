from PySide import QtGui
from gen.config import Ui_ConfigForm
from config_bundle import BundleWidget
from resourceswindow import ResourcesWindow
from variableswindow import VariablesWindow
from models import ResourcesListModel, VariablesListModel
from pprint import pprint
import os
import json
import copy

class ConfigWidget(QtGui.QWidget):
  def __init__(self, *args, **kwargs):
    super(ConfigWidget, self).__init__(*args, **kwargs)
  
  def get_config(self):
    raise NotImplementedError("Abstract method is not implemented")

class ConfigForm(ConfigWidget, Ui_ConfigForm):
  
  def __init__(self, config, *args, **kwargs):
    super(ConfigForm, self).__init__(*args, **kwargs)
    self.setupUi()
    self.__config__ = config
    self.bundles =[]
    self.bind_controls()
    self.save_path = None
    
    #pprint(self.get_dict())
  def set_save_path(self, path):
    self.save_path = path
    
  def setupUi(self):
    super(ConfigForm, self).setupUi(self)
    self.variables_widget = VariablesWindow(self)
    self.variables_widget.lv_items.set_object_format("application/x-variable")
    
    self.resources_widget = ResourcesWindow(self)
    self.resources_widget.lv_resources.set_object_format("application/x-resource")
    
    self.lt_variables.addWidget(self.variables_widget)
    self.lt_resources.addWidget(self.resources_widget)
  
  def bind_controls(self):
    self.resources_widget.setModel(ResourcesListModel(self.get_config()["Resources"]))
    self.variables_widget.setModel(VariablesListModel(self.get_config()["Variables"]))
    self.btn_save.clicked.connect(self.save_config)
    self.setup_bundles()

  def setup_bundles(self):
    self.la_name.setText(self.get_config()["PublisherId"])
    bundles = self.tlbx_bundles
    bundles.removeItem(0)
    bundles.removeItem(0)
    for bundle in self.get_config()["Content"]["OperationBundles"]:
      self.add_bundle(bundle)
    
  def add_bundle(self, bundle):
    self.bundles.append(BundleWidget(bundle, self))
    self.tlbx_bundles.addItem(self.bundles[-1], bundle["Name"])
    
  def get_config(self):
    return self.__config__
  
  def save_config(self):
    sp,  _ = QtGui.QFileDialog.getSaveFileName(self, 'Choose destination file', self.save_path or "~")
    if sp:
      self.save_path = sp
      print "saved file on "+self.save_path
      f = open(self.save_path,"w")
      d = self.get_dict()
      
      if d["Content"].has_key("Reference"):
        print "writing the referenced file"
        p = d["Content"]["Reference"]
        content = copy.deepcopy(d["Content"])
        d["Content"]={"Reference":p}
        del content["Reference"]
        ref_file = os.path.join(os.path.dirname(sp), p)
        rf = open(ref_file,"w")
        rf.write(json.dumps(content, sort_keys = True, indent = 2))
        rf.close()
      f.write(json.dumps(d, sort_keys = True, indent = 2))
      f.close()
    else:
      print "Saving cancelled"

  def get_dict(self):
    d = {"PublisherId": self.la_name.text()}
    d["Content"] = {}
    bundles = d["Content"]["OperationBundles"]=[]
    for bw in self.bundles:
      bundles.append(bw.get_dict())
    d["Resources"]= self.resources_widget.data_model.resources
    d["Variables"]=self.variables_widget.data_model.resources
    if self.__config__["Content"].has_key("Reference"):
      d["Content"]["Reference"] = self.__config__["Content"]["Reference"]
    return d
  

