from PySide import QtGui
import os
from hal_configurator.ui.gen.resources_widget import Ui_ResourcesWidget
from hal_configurator.lib.workspace_manager import Workspace
from hal_configurator.ui.models import ResourcesListModel, VariablesListModel
class ResourcesWidget(QtGui.QWidget, Ui_ResourcesWidget):
  def __init__(self, *args, **kwargs):
    super(ResourcesWidget, self).__init__(*args, **kwargs)
    self._model = None
    self.setupUi()
    self.bindUi()
  
  def setModel(self, model):
    visibility_settings = UIVisibilitySettings.settings_for_mode(Workspace.current.mode)  # @UndefinedVariable
    self._model = model
    self.lv_vars.set_object_format("application/x-variable")
    self.lv_resources.set_object_format("application/x-resource")
    self.lv_resources.setModel(ResourcesListModel(model["Resources"], self.root_dir))
    self.lv_vars.setModel(VariablesListModel(model["Variables"], visibility_settings))
    self.lv_vars.setMode(Workspace.current.mode)
    
    
  def model(self):
    return self._model
    
  def setupUi(self):
    super(ResourcesWidget, self).setupUi(self)
  
  def bindUi(self):
    pass