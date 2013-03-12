from PySide import QtGui

class OperationWidget(QtGui.QPushButton):
  def __init__(self, *args, **kwargs):
    super(OperationWidget, self).__init__()
    self.setDragEnabled(True)