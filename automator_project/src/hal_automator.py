#!/usr/bin/env python
import sys
import os

from hal_configurator.lib.app_config import config
from hal_configurator.lib.plugin_loader import load_plugins_from_directory_list

if config:
  load_plugins_from_directory_list(config.plugin_dirs)
else:
  print 'No Configuration Loadeed, Continuing...'

sys.path.append(os.path.abspath(__file__))
try:
  import hal_configurator.lib.configurator_console as console
except:
  print 'Not configured for executor, only web server mode is possible'
try:
  import hal_configurator.web.web_server as web_server
except:
  print 'Not Configured for web mode'

ui_enabled= True
try:
  from PySide import QtGui
except Exception, ex:
  ui_enabled = False
  print ex
  print "No Qt Installed"
if ui_enabled:
  from hal_configurator.ui.configwindow import ConfigWindow

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
  elif sys.argv[1]=='-web':
    web_server.run_server()
