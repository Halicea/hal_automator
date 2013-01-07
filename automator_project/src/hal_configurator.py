import sys, os
sys.path.append(os.path.abspath(__file__))
import lib.configurator_console as console

try:
  from PySide import QtGui
  from ui.mainwindow import MainWindow
except:
  print "No PySide found"

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
