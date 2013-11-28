
from PySide import QtGui
from hal_configurator.ui.gen.confirm_dialog import Ui_ConfirmDialog

class ConfirmDialog(QtGui.QDialog, Ui_ConfirmDialog):

  def __init__(self, message,*args, **kwargs):
#    self.accepted = QtCore.Signal()
#    self.rejected = QtCore.Signal()
    super(ConfirmDialog, self).__init__(*args, **kwargs)
    self.message = message
    self.setupUi()
    self.bindUi()

  def setupUi(self):
    super(ConfirmDialog, self).setupUi(self)
    self.la_confirm_message.setText(self.message)
  
  def bindUi(self):
    pass