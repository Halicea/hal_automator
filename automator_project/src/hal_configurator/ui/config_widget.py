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
from hal_configurator.ui.uiutils import UIVisibilitySettings

class ConfigWidget(QtGui.QWidget):
  def __init__(self, *args, **kwargs):
    super(ConfigWidget, self).__init__(*args, **kwargs)

  def get_config(self):
    raise NotImplementedError("Abstract method is not implemented")





class ConfigForm(ConfigWidget, Ui_ConfigForm):

  def __init__(self, config_loader, parent=None, details_parent = None, *args, **kwargs):
    super(ConfigForm, self).__init__(*args, **kwargs)
    self.setupUi()
    self.config_loader = config_loader
    self.__config__ = self.config_loader.load_config()
    self.root_dir = os.path.dirname(self.config_loader.config_file)
    self.save_path = self.config_loader.config_file
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
    visibility_settings = UIVisibilitySettings.settings_for_mode(Workspace.current.mode)  # @UndefinedVariable
    self.resources_widget.setModel(ResourcesListModel(self.get_config()["Resources"], self.root_dir))
    self.variables_widget.setModel(VariablesListModel(self.get_config()["Variables"], visibility_settings))
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

  def extend_var(self, target, src, excluded_keys=[]):
    for k in src.keys():
      if not (k in excluded_keys):
        if k == 'value':
          print 'wrong here'
        if k in target:
          if src[k]!=None and src[k]!=target[k]:
            target[k] = src[k]
        else:
          target[k]= src[k]
    return target

  def sanitize_vars(self, d, clean_required_vars = True, update_global_vars=False, wipe_var_values=False):
    rvars = d['RequiredVariables']
    if update_global_vars:
      for v in d['Variables']:
        editable = True if not ('editable' in v) else v['editable']
        found = [rv for rv in rvars if rv['name']==v['name']]
        excluded_keys = ['is_from_req']
        if editable:
          excluded_keys.append('value')
        if found:
          self.extend_var(found[0], v, excluded_keys)
        else:
          rvars.append(self.extend_var({}, v, excluded_keys))
      to_del = []
      for rv in rvars:
        found = [v for v in d['Variables'] if v['name']==rv['name'] and v['required']]
        if not found:
          to_del.append(rv)
      for k in to_del:
        del rv[k]

    if clean_required_vars:
      to_remove = []
      for v in d['Variables']:
        found = [rv for rv in rvars if rv['name']==v['name']]
        if found:
          if found[0].has_key('editable') and not found[0]['editable']:
            to_remove.append(v)
          elif found[0]['value'] == v['value']:
            to_remove.append(v)
      for v in to_remove:
        d['Variables'].remove(v)

    if wipe_var_values:
      for v in d['Variables']:
        found = [rv for rv in rvars if rv['name']==v['name']]
        if found:
          v['value'] = found[0]['value']
        else:
          v['value'] = None

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
      d = copy.deepcopy(self.get_dict())
      save_references = Workspace.current.mode=='admin'
      self.sanitize_vars(d, clean_required_vars=True, update_global_vars=save_references,wipe_var_values=is_cloning_empty)
        # @UndefinedVariable
      self.config_loader.save_config(d, save_references)
    else:
      print "Saving cancelled"
    self.save_path = old_path

  def get_dict(self):
    d = copy.deepcopy(self.__config__)
    d["PublisherId"]= self.txt_name.text()
    bundles = d["Content"]["OperationBundles"]=[]
    for bw in self.bundles:
      bundles.append(bw.get_dict())
    d["Resources"]= copy.deepcopy(self.resources_widget.data_model.resources)
    d["Variables"]=copy.deepcopy(self.variables_widget.data_model.resources)
    return d

