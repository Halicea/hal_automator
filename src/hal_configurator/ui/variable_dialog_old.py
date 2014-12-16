
from PySide import QtGui
from gen.variable_dialog_old import Ui_Dialog

class Dialog(QtGui.QWidget, Ui_Dialog):
  def __init__(self, *args, **kwargs):
    super(Dialog, self).__init__(*args, **kwargs)
    self.setupUi()
    self.bindUi()

  def setupUi(self):
    super(Dialog, self).setupUi(self)

  def bindUi(self):
    pass
