
from PySide import QtGui
from gen.ime_test import Ui_ImeForm

class ImeForm(QtGui.QWidget, Ui_ImeForm):
  def __init__(self, *args, **kwargs):
    super(ImeForm, self).__init__(*args, **kwargs)
    self.setupUi()
    self.bindUi()
    
  def setupUi(self):
    super(ImeForm, self).setupUi(self)
    
  def bindUi(self):
    self.pushButton.clicked.connect(self.on_clicked)
    
