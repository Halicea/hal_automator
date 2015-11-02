from PySide import QtGui
import os

from hal_configurator.ui.gen.resources_widget import Ui_ResourcesWidget
from hal_configurator.lib.workspace_manager import Workspace
from hal_configurator.ui.models import ResourcesListModel, VariablesListModel
from hal_configurator.ui.uiutils import UIVisibilitySettings

class ResourcesWidget(QtGui.QWidget, Ui_ResourcesWidget):
  def __init__(self, *args, **kwargs):
    super(ResourcesWidget, self).__init__(*args, **kwargs)
    self._model = None
    self.setupUi()
    self.bindUi()
  
  def setModel(self, model, root_dir):
    visibility_settings = UIVisibilitySettings.settings_for_mode(Workspace.current.mode)  # @UndefinedVariable
    self._model = model
    self.lv_resources.setModel(ResourcesListModel(model["Resources"], root_dir), root_dir)
    self.lv_variables.setModel(VariablesListModel(model["Variables"], visibility_settings))
    self.lv_variables.setMode(Workspace.current.mode)

  def model(self):
    return self._model
    
  def setupUi(self):
    super(ResourcesWidget, self).setupUi(self)
  
  def bindUi(self):
    pass
  
  def get_dict(self):
    d = {}
    d["Resources"] = copy.deepcopy(self.lv_resources.data_model.resources)
    d["Variables"] = copy.deepcopy(self.lv_variables.data_model.resources)
    return d