from PySide import QtGui, QtCore
from hal_configurator.ui.gen.config_widget import Ui_ConfigForm
from config_bundle import BundleWidget
from resourceswindow import ResourcesWindow
from variableswindow import VariablesWindow
from models import ResourcesListModel, VariablesListModel
import os
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
  def __init__(self, config_loader, parent=None, details_parent=None, *args, **kwargs):
    super(ConfigForm, self).__init__(*args, **kwargs)
    self.setupUi()
    self.config_loader = config_loader
    self.__config__ = self.config_loader.load_config()
    self.root_dir = os.path.dirname(self.config_loader.config_file)
    self.save_path = self.config_loader.config_file
    self.details_parent = details_parent or None
    self.bundles = []
    self.parent = parent
    self.bind_controls()

  def setupUi(self):
    super(ConfigForm, self).setupUi(self)

  def bind_controls(self):
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

  def get_dict(self):
    d = {
          "PublisherId":self.txt_name.text(),
          "OperationBundles":[]
         }
    bundles = d["OperationBundles"]
    for bw in self.bundles:
      bundles.append(bw.get_dict())
    return d
