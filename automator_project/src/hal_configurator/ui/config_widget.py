from PySide import QtGui, QtCore
from hal_configurator.ui.gen.config import Ui_ConfigForm
from config_bundle import BundleWidget
from resourceswindow import ResourcesWindow
from variableswindow import VariablesWindow
from models import ResourcesListModel, VariablesListModel
import os
import json
import copy
from hal_configurator.lib.workspace_manager import Workspace
from shutil import copytree

class ConfigWidget(QtGui.QWidget):
  def __init__(self, *args, **kwargs):
    super(ConfigWidget, self).__init__(*args, **kwargs)

  def get_config(self):
    raise NotImplementedError("Abstract method is not implemented")





class ConfigForm(ConfigWidget, Ui_ConfigForm):

  def __init__(self, config, config_path, parent=None, details_parent = None, *args, **kwargs):
    super(ConfigForm, self).__init__(*args, **kwargs)
    self.setupUi()
    self.__config__ = config
    self.root_dir = os.path.dirname(config_path)
    self.save_path = config_path
    self.details_parent = details_parent or None
    self.bundles =[]
    self.parent = parent
    self.bind_controls()

    #pprint(self.get_dict())
  def set_save_path(self, path):
    self.save_path = path

  def setupUi(self):
    super(ConfigForm, self).setupUi(self)


  def bind_controls(self):
    self.variables_widget = VariablesWindow(self)
    if self.details_parent:
      self.variables_widget.setDetailsContainer(self.details_parent)
    self.variables_widget.lv_items.set_object_format("application/x-variable")

    self.resources_widget = ResourcesWindow(self.root_dir, self)
    if self.details_parent:
      self.resources_widget.setDetailsContainer(self.details_parent)
    self.resources_widget.lv_resources.set_object_format("application/x-resource")

    self.lt_variables.addWidget(self.variables_widget)
    self.lt_resources.addWidget(self.resources_widget)

    self.resources_widget.setModel(ResourcesListModel(self.get_config()["Resources"], self.root_dir))
    self.variables_widget.setModel(VariablesListModel(self.get_config()["Variables"]))
    self.variables_widget.setMode(Workspace.current.mode)  # @UndefinedVariable
    self.btn_save.clicked.connect(self.save_config)
    self.btn_save.clicked.connect(lambda x: self.save_config(True))
    self.setup_bundles()

  def setup_bundles(self):
    self.txt_name.setText(self.get_config()["PublisherId"])
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

  @QtCore.Slot()
  def ensure_in_workspace(self, current):
    root = self.parent.workspace.workspacedir
    wd = os.path.realpath(root)
    cd = os.path.realpath(current)
    in_workspace = False
    if cd:
      in_workspace = cd.startswith(wd)

    if not in_workspace:
      print 'not in workspace', current
      self.dlg.setDirectory(wd)
    else:
      print 'in workspace'


  def cleanup_required_vars(self, d, required_vars):
    rvars = self.get_config()['RequiredVariables']
    for v in d['Variables']:
      found = [rv for rv in rvars if rv['name']==v['name']]
      if found:
        if found[0].has_key('editable') and not found[0]['editable']:
          d['Variables'].remove(v)
        elif found[0]['value'] == v['value']:
          d['Variables'].remove(v)





  @QtCore.Slot()
  def save_config(self, is_new=False, is_cloning_empty=False):
    sp  = self.save_path
    old_path = self.save_path
    if self.save_path == None or is_new:
      self.dlg = QtGui.QFileDialog(self, 'Choose where to save the project')

      self.dlg.setAcceptMode(QtGui.QFileDialog.AcceptSave)
      self.dlg.currentChanged.connect(self.ensure_in_workspace)
      if self.dlg.exec_() == QtGui.QFileDialog.Rejected:
        return
      sp = self.dlg.selectedFiles()[0]
      self.dlg = None
    if sp:
      if is_new and self.save_path!=sp:
        if not is_cloning_empty:
          copytree(self.root_dir, os.path.dirname(sp))
        self.save_path = sp
      print "saving file on "+self.save_path
      f = open(self.save_path,"w")
      d = copy.deepcopy(self.get_dict())
      rvars = self.get_config()['RequiredVariables']
      self.cleanup_required_vars(d, rvars)
      if is_cloning_empty:
        for v in d['Variables']:
          found = [rv for rv in rvars if rv['name']==v['name']]
          if found:
            v['value'] = found[0]['value']
          else:
            v['value'] = None

      if d["Content"].has_key("Reference"):
        print "writing the referenced file"
        p = d["Content"]["Reference"]
        content = copy.deepcopy(d["Content"])
        ref_location = os.path.abspath(os.path.join(os.path.dirname(old_path), p))
        current_location = os.path.abspath(os.path.dirname(sp))
        d["Content"]={"Reference":os.path.relpath(ref_location, current_location) }
        del content["Reference"]
        ref_file = os.path.join(os.path.dirname(sp), p)
        rf = open(ref_file,"w")
        rf.write(json.dumps(content, sort_keys = True, indent = 2))
        rf.close()
      f.write(json.dumps(d, sort_keys = True, indent = 2))
      f.close()
    else:
      print "Saving cancelled"
    self.save_path = old_path

  def get_dict(self):
    d = {"PublisherId": self.txt_name.text()}
    #d["_id"] = self.__config__["_id"]
    if "RequiredVariables-Reference" in self.__config__:
      d["RequiredVariables"] = self.__config__["RequiredVariables-Reference"]
    else:
      d["RequiredVariables"] = self.__config__["RequiredVariables"]

    d["Content"] = {}
    bundles = d["Content"]["OperationBundles"]=[]
    for bw in self.bundles:
      bundles.append(bw.get_dict())
    d["Resources"]= self.resources_widget.data_model.resources
    d["Variables"]=self.variables_widget.data_model.resources
    if self.__config__["Content"].has_key("Reference"):
      d["Content"]["Reference"] = self.__config__["Content"]["Reference"]
    return d

