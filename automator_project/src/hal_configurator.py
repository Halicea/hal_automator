from PySide import QtGui
import sys
from ui.mainwindow import MainWindow
import lib.configurator_console as console

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