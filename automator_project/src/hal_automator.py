#!/usr/bin/env python
import sys
import os

from hal_configurator.lib.app_config import config
from hal_configurator.lib.plugin_loader import load_plugins_from_directory_list

load_plugins_from_directory_list(config.plugin_dirs)
sys.path.append(os.path.abspath(__file__))
import hal_configurator.lib.configurator_console as console
try:
  from PySide import QtGui
  from hal_configurator.ui.configwindow import ConfigWindow
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
  # app.setStyle(QtGui.QWindowsStyle)
  mw = ConfigWindow(None)
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
