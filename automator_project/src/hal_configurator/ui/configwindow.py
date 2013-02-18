
from PySide import QtGui
from hal_configurator.lib.config_loaders import FileConfigLoader
from gen.configwindow import Ui_ConfigWindow
from config import ConfigForm
from hal_configurator.ui.models import ToolsListModel
import hal_configurator.plugins as plugins

class ConfigWindow(QtGui.QMainWindow, Ui_ConfigWindow):
  config = None
  def __init__(self, config_path, working_dir, *args, **kwargs):
    super(ConfigWindow, self).__init__(*args, **kwargs)
    self.config_path = config_path
    self.working_dir = working_dir
    ConfigWindow.config = FileConfigLoader(self.config_path).load_config()
    self.cw = None
    self.setupUi()
    self.bindUi()
    
  def setupUi(self):
    super(ConfigWindow, self).setupUi(self)
    self.cw = ConfigForm(self.config, self)
    self.ltv_content.addWidget(self.cw)
    self.tool = QtGui.QListView(self)
    self.tool.setModel(ToolsListModel(plugins.__all__, False))
    self.lv_tools.addWidget(self.tool)
    self.splitter.setSizes([self.splitter.height(), 0])
    self.splitter_2.setSizes([self.splitter_2.width(), 0])
    self.btnRun.clicked.connect(self.on_clicked_click)
    self.txtWorkingDir.setText(self.working_dir)

    #layout = QtGui.QVBoxLayout()
    #layout.addWidget(self.cw)

  def bindUi(self):
    pass

  def on_clicked_click(self):
    pass

