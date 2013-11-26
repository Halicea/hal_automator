
from PySide import QtGui
from hal_configurator.ui.gen.tool_set import Ui_ToolSet
import hal_configurator.plugins as plugins
from hal_configurator.lib.plugin_loader import get_plugins_list
from models import ToolsListModel

class ToolSet(QtGui.QWidget, Ui_ToolSet):
  def __init__(self, *args, **kwargs):
    super(ToolSet, self).__init__(*args, **kwargs)
    
    self.setupUi()
    self.bindUi()

  def setupUi(self):
    super(ToolSet, self).setupUi(self)
    

  def bindUi(self):
    plugins = get_plugins_list()
    model = ToolsListModel(plugins)
    self.lv_tools.setModel(model)
      
      
