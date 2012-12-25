
from PySide import QtGui
from gen.configwindow import Ui_ConfigWindow
from config import ConfigForm
class ConfigWindow(QtGui.QMainWindow, Ui_ConfigWindow):
  config = None
  def __init__(self, config, *args, **kwargs):
    super(ConfigWindow, self).__init__(*args, **kwargs)
    self.config = config
    ConfigWindow.config = config
    self.cw = None
    self.setupUi()
    self.bindUi()
    
  def setupUi(self):
    super(ConfigWindow, self).setupUi(self)
    self.cw = ConfigForm(self.config, self)
    self.ltv_content.addWidget(self.cw)
    #layout = QtGui.QVBoxLayout()
    #layout.addWidget(self.cw)
  def bindUi(self):
    pass
