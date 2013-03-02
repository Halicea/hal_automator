
from PySide import QtGui, QtCore
from PySide.QtCore import QDir
from PySide.QtGui import QFileSystemModel
from gen.config_manager import Ui_ConfigManager
import os
from hal_configurator.ui.configwindow import ConfigWindow

config_path = '/Users/kostamihajlov/MyProjects/PrintStandClient/src/Configs'
class ConfigManager(QtGui.QWidget, Ui_ConfigManager):
  def __init__(self, *args, **kwargs):
    super(ConfigManager, self).__init__(*args, **kwargs)
    self.setupUi()
    self.bindUi()
    self.windows = {}

  def setupUi(self):
    super(ConfigManager, self).setupUi(self)

  def bindUi(self):
    self.btnPublish.clicked.connect(self.publish_clicked)
    self.model = QFileSystemModel()
    self.model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)
    self.model.setRootPath(config_path)


    self.treeView.setModel(self.model)
    self.treeView.setRootIndex(self.model.index(config_path))
    self.treeView.setAnimated(True);
    self.treeView.setIndentation(20);
    self.treeView.setSortingEnabled(True);
    self.treeView.setWindowTitle("Branded App Configurations")
    #self.treeView.set
    #self.treeView.setAllColumnsShowFocus(False);
    self.treeView.doubleClicked.connect(self.config_selected)


  @QtCore.Slot()
  def publish_clicked(self):
    index = self.treeView.currentIndex()
    #self.model.

  @QtCore.Slot()
  def config_selected(self):
    print "Config is selected"
    p = self.model.filePath(self.treeView.currentIndex())
    config_path = os.path.join(p, "bc.json")
    if os.path.exists(config_path):
      if not config_path in self.windows:
        c = ConfigWindow(config_path, None)
        c.closeEvent = lambda x: self.windows.pop(config_path)
        self.windows[config_path] = c
      self.windows[config_path].show()


