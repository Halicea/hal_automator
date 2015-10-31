
from PySide import QtGui
from hal_configurator.ui.gen.console_output import Ui_ConsoleOutput

class ConsoleOutput(QtGui.QWidget, Ui_ConsoleOutput):
  def __init__(self, *args, **kwargs):
    super(ConsoleOutput, self).__init__(*args, **kwargs)
    self.setupUi()
    self.bindUi()

  def setupUi(self):
    super(ConsoleOutput, self).setupUi(self)

  def bindUi(self):
    self.btn_clear.clicked.connect(self.clear_output)

  def clear_output(self):
    self.txt_output.clear()