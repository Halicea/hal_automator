#!/usr/bin/env python
import sys, os

from hal_configurator.ui.tool_set import ToolSet
sys.path.append(os.path.abspath(__file__))
import hal_configurator.lib.configurator_console as console
try:
  from PySide import QtGui, QtCore
  #from hal_configurator.ui.config_chooser import ConfigChooserWidget
  from hal_configurator.ui.mainwindow import MainWindow
except Exception, ex:
  print ex
  print "No Qt Installed"
  print "Continuing in ConsoleMode"
  
def main():
  app = QtGui.QApplication(sys.argv)
  mw = MainWindow()
  mw.show()
  app.setWindowIcon(QtGui.QIcon())
  sys.exit(app.exec_())

if __name__ == "__main__":
  if len(sys.argv)==1:
    main()
  else:
    console.main()
