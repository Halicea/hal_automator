from PySide import QtGui, QtCore
from hal_configurator.ui.gen.directory_chooser_widget import Ui_DirectoryChooserWidget

class DirectoryChooserWidget(QtGui.QWidget, Ui_DirectoryChooserWidget):
  
  def __init__(self, message,*args, **kwargs):
    super(DirectoryChooserWidget, self).__init__(*args, **kwargs)
    self.setupUi()
    self.bindUi()
    self.title = "Choose directory"
  def setupUi(self):
    super(DirectoryChooserWidget, self).setupUi(self)
  
  def bindUi(self):
    pass
  
  @QtCore.Slot()
  def chooseDirectory(self):
    res = QtGui.QFileDialog.getExistingDirectory(caption=self.title)
    if res:
      self.txt_dir.setText(res)
  
  def setText(self, value):
    self.txt_dir.setText(value)
  
  def text(self):
    return self.txt_dir.text() or ''