
from PySide import QtGui
from gen.variable_dialog import Ui_Dialog

class Dialog(QtGui.QDialog, Ui_Dialog):
  def __init__(self, *args, **kwargs):
    super(Dialog, self).__init__(*args, **kwargs)
    self.setupUi()
    self.bindUi()

  def get_variable(self):
    return {"name":self.txt_name.text(), "value":self.txt_value.text()}
  
  def setupUi(self):
    super(Dialog, self).setupUi(self)

  def bindUi(self):
    pass
