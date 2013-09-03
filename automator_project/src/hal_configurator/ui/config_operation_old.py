
from PySide import QtGui
from hal_configurator.ui.gen.config_operation_old import Ui_OperationWidget

class OperationWidget(QtGui.QWidget, Ui_OperationWidget):
  def __init__(self, *args, **kwargs):
    super(OperationWidget, self).__init__(*args, **kwargs)
    self.setupUi()
    self.bindUi()

  def setupUi(self):
    super(OperationWidget, self).setupUi(self)

  def bindUi(self):
    pass
