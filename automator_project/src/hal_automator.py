#!/usr/bin/env python
import sys
import os
from hal_configurator.lib.app_config import config
from hal_configurator.lib.plugin_loader import load_plugins_from_directory_list
load_plugins_from_directory_list(config.plugin_dirs)
sys.path.append(os.path.abspath(__file__))
import hal_configurator.lib.configurator_console as console
from hal_configurator.ui.config_manager import ConfigManager
try:
  from PySide import QtGui, QtCore, QtCore
  from PySide.QtGui import  QCloseEvent
  from hal_configurator.ui.mainwindow import MainWindow
except Exception, ex:
  print ex
  print "No Qt Installed"
  print "Continuing in ConsoleMode"
  
def main(isAdmin):
  """
  Main Application Runner
  :param: isAdmin
  :type : isAdmin: bool
  """
  app = QtGui.QApplication(sys.argv)
  #"windows", "motif", "cde", "plastique", "windowsxp", or "macintosh"
  #app.setStyle("macintosh")
  mw = ConfigManager()
  if isAdmin:
    mw = MainWindow()
  mw.show()
  app.setWindowIcon(QtGui.QIcon())
  sys.exit(app.exec_())



if __name__ == "__main__":
  if len(sys.argv)==1 :
    main(False)
  elif sys.argv[1] =='-admin':
    main(True)
  else:
    console.main()


