
from PySide import QtGui
from hal_configurator.ui.gen.regex_tool import Ui_RegexTool
import re
class RegexTool(QtGui.QWidget, Ui_RegexTool):
  def __init__(self, *args, **kwargs):
    super(RegexTool, self).__init__(*args, **kwargs)
    self.setupUi()
    self.bindUi()

  def setupUi(self):
    super(RegexTool, self).setupUi(self)

  def bindUi(self):
    self.btnRun.clicked.connect(self.btnRun_clicked)
  
  def btnRun_clicked(self):
    rem = re.compile(self.txtRegex.text())
    if self.cbMultiLine.checkState():
      rem = re.compile(self.txtRegex.text(), re.DOTALL)
    test = self.txtTest.toPlainText()
    res = re.findall(rem, test) 
    result = re.sub(rem, self.txtReplaceWith.text(), test, len(res))
    self.txtResult.setPlainText(result)
    
    
