import os
from PySide import QtGui, QtCore
from hal_configurator.ui.gen.config_manager import Ui_ConfigManager
from PySide.QtCore import QDir, QEvent
from PySide.QtGui import QFileSystemModel

from hal_configurator.ui.configwindow import ConfigWindow
from hal_configurator.lib import app_config


class ConfigManager(QtGui.QMainWindow, Ui_ConfigManager):
  def __init__(self, *args, **kwargs):
    super(ConfigManager, self).__init__(*args, **kwargs)
    self.setupUi()
    self.bindUi()
    self.windows = {}

  def setupUi(self):
    super(ConfigManager, self).setupUi(self)

  def bindUi(self):
    self.model = QFileSystemModel()
    self.model.setRootPath("/")
    self.model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)
    self.treeView.setModel(self.model)
    if app_config.get_last_dir():
      self.treeView.setCurrentIndex(self.model.index(app_config.get_last_dir()))
    self.treeView.setAnimated(True)
    self.treeView.setIndentation(20)
    self.treeView.setSortingEnabled(True)
    self.treeView.setWindowTitle("Branded App Configurations")
    self.treeView.doubleClicked.connect(self.config_selected)
    self.set_recent_config_actions()

  def set_recent_config_actions(self):
    history = app_config.get_config_history()
    self.historyActions = []
    for k in history:
      a = QtGui.QAction(self)
      a.triggered.connect(lambda: self.open_config(k))
      a.setText(k)
      self.historyActions.append(a)
      self.menuRecent.addAction(a)

  @QtCore.Slot()
  def publish_clicked(self):
    index = self.treeView.currentIndex()
    pass

  def open_config(self, config_path):
    if os.path.exists(config_path):
      app_config.set_last_dir(os.path.dirname(config_path))
      if not config_path in self.windows:
        c = ConfigWindow(self)
        c.set_configuration(config_path, None)
        app_config.add_config_to_history(config_path)
        c.closeEvent = lambda x: self.windows.pop(config_path)
        self.windows[config_path] = c
      self.windows[config_path].show()

  @QtCore.Slot()
  def config_selected(self):
    print "Config is selected"
    p = self.model.filePath(self.treeView.currentIndex())
    config_path = os.path.join(p, "bc.json")
    config_path = config_path.replace('\\', '/')
    self.open_config(config_path)