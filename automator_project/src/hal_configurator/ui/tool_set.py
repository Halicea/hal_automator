
from PySide import QtGui
from hal_configurator.ui.gen.tool_set import Ui_ToolSet
import hal_configurator.plugins as plugins
from models import ToolsListModel

class ToolSet(QtGui.QWidget, Ui_ToolSet):
  def __init__(self, *args, **kwargs):
    super(ToolSet, self).__init__(*args, **kwargs)
    
    self.setupUi()
    self.bindUi()

  def setupUi(self):
    super(ToolSet, self).setupUi(self)
    

  def bindUi(self):
    model = ToolsListModel(plugins.__all__)
    self.lv_tools.setModel(model)
      
      
