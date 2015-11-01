from PySide import QtGui, QtCore
from hal_configurator.ui.gen.directory_chooser_widget import Ui_DirectoryChooserWidget

class DirectoryChooserWidget(QtGui.QWidget, Ui_DirectoryChooserWidget):
  
  def __init__(self, message,*args, **kwargs):
    super(DirectoryChooserWidget, self).__init__(*args, **kwargs)

  def setupUi(self):
    pass
  
  def bindUi(self):
    pass