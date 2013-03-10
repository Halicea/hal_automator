import os
from PySide import QtGui, QtCore
from gen.config_manager import Ui_ConfigManager
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
        c = ConfigWindow(self, config_path, None)
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

  def focusInEvent(self, *args, **kwargs):
    super(ConfigManager, self).focusInEvent(*args, **kwargs)
    self.set_manager_menu()
    self.bindUi()

  def eventFilter(self, object, filter):
    if filter.eventType == QEvent.FocusIn:
      if isinstance(object, ConfigManager):
        self.set_manager_menu()
      else:
        self.set_manager_menu()

  def set_manager_menu(self):
    self.menubar.clear()
    self.menuFile = QtGui.QMenu(self.menubar)
    self.menuFile.setObjectName("menuFile")
    self.menuEdit = QtGui.QMenu(self.menubar)
    self.menuEdit.setObjectName("menuEdit")
    ConfigManager.setMenuBar(self.menubar)
    self.statusbar = QtGui.QStatusBar(ConfigManager)
    self.statusbar.setObjectName("statusbar")
    self.setStatusBar(self.statusbar)
    self.actionClone = QtGui.QAction(ConfigManager)
    self.actionClone.setObjectName("actionClone")
    self.actionPreferences = QtGui.QAction(ConfigManager)
    self.actionPreferences.setObjectName("actionPreferences")
    self.menuFile.addAction(self.actionClone)
    self.menuEdit.addAction(self.actionPreferences)
    self.menubar.addAction(self.menuFile.menuAction())
    self.menubar.addAction(self.menuEdit.menuAction())
    self.menuFile.setTitle(QtGui.QApplication.translate("ConfigManager", "File", None, QtGui.QApplication.UnicodeUTF8))
    self.menuEdit.setTitle(QtGui.QApplication.translate("ConfigManager", "Edit", None, QtGui.QApplication.UnicodeUTF8))
    self.actionClone.setText(QtGui.QApplication.translate("ConfigManager", "Clone", None, QtGui.QApplication.UnicodeUTF8))
    self.actionPreferences.setText(QtGui.QApplication.translate("ConfigManager", "Preferences", None, QtGui.QApplication.UnicodeUTF8))

  def set_config_menu(self):
    self.menubar.clear()
    self.menuFile = QtGui.QMenu(self.menubar)
    self.menuFile.setObjectName("menuFile")
    self.menuEdit = QtGui.QMenu(self.menubar)
    self.menuEdit.setObjectName("menuEdit")
    self.menuHelp = QtGui.QMenu(self.menubar)
    self.menuHelp.setObjectName("menuHelp")
    self.setMenuBar(self.menubar)
    self.statusbar = QtGui.QStatusBar(self)
    self.statusbar.setObjectName("statusbar")
    self.setStatusBar(self.statusbar)
    self.actionSave = QtGui.QAction(self)
    self.actionSave.setObjectName("actionSave")
    self.actionRun = QtGui.QAction(self)
    self.actionRun.setObjectName("actionRun")
    self.actionCopy_2 = QtGui.QAction(self)
    self.actionCopy_2.setObjectName("actionCopy_2")
    self.actionPaste = QtGui.QAction(self)
    self.actionPaste.setObjectName("actionPaste")
    self.actionAbout = QtGui.QAction(self)
    self.actionAbout.setObjectName("actionAbout")
    self.actionSave_As = QtGui.QAction(self)
    self.actionSave_As.setObjectName("actionSave_As")
    self.actionClose = QtGui.QAction(self)
    self.actionClose.setObjectName("actionClose")
    self.actionClone = QtGui.QAction(self)
    self.actionClone.setObjectName("actionClone")
    self.menuFile.addAction(self.actionSave)
    self.menuFile.addAction(self.actionSave_As)
    self.menuFile.addAction(self.actionClone)
    self.menuFile.addAction(self.actionRun)
    self.menuFile.addSeparator()
    self.menuFile.addAction(self.actionClose)
    self.menuEdit.addAction(self.actionCopy_2)
    self.menuEdit.addAction(self.actionPaste)
    self.menuHelp.addAction(self.actionAbout)
    self.menubar.addAction(self.menuFile.menuAction())
    self.menubar.addAction(self.menuEdit.menuAction())
    self.menubar.addAction(self.menuHelp.menuAction())
    self.menuFile.setTitle(QtGui.QApplication.translate("ConfigWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
    self.menuEdit.setTitle(QtGui.QApplication.translate("ConfigWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
    self.menuHelp.setTitle(QtGui.QApplication.translate("ConfigWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
    self.actionSave.setText(QtGui.QApplication.translate("ConfigWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
    self.actionSave.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
    self.actionRun.setText(QtGui.QApplication.translate("ConfigWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
    self.actionRun.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
    self.actionCopy_2.setText(QtGui.QApplication.translate("ConfigWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
    self.actionCopy_2.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
    self.actionPaste.setText(QtGui.QApplication.translate("ConfigWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
    self.actionPaste.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
    self.actionAbout.setText(QtGui.QApplication.translate("ConfigWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
    self.actionSave_As.setText(QtGui.QApplication.translate("ConfigWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
    self.actionSave_As.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
    self.actionClose.setText(QtGui.QApplication.translate("ConfigWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
    self.actionClose.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
    self.actionClone.setText(QtGui.QApplication.translate("ConfigWindow", "Clone", None, QtGui.QApplication.UnicodeUTF8))
    self.actionClone.setShortcut(QtGui.QApplication.translate("ConfigWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))



