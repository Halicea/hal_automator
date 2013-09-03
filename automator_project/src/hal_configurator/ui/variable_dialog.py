
from PySide import QtGui
from hal_configurator.ui.gen.variable_dialog import Ui_Dialog
from hal_configurator.ui.models import SimpleStringListModel


class VariableDialog(QtGui.QDialog, Ui_Dialog):
  def __init__(self, *args, **kwargs):
    super(VariableDialog, self).__init__(*args, **kwargs)
    self.model = None
    self.types_model = ["text", "file", "color","bool", "url"]
    self.setupUi()
    self.bindUi()

  def setupUi(self):
    super(VariableDialog, self).setupUi(self)

  def setModel(self, model):
    self.model = model
    t = "text"
    if self.model.has_key("type"):
      t = self.model["type"]
    self.txt_name.setText(self.model["name"])
    self.txt_value.setText(self.model["value"])
    self.cmbType.setCurrentIndex(self.types_model.index(t))

  def bindUi(self):
    self.cmbType.setModel(SimpleStringListModel(self.types_model))
    self.txt_value.textChanged.connect(self.valueChanged)
    self.txt_name.textChanged.connect(self.nameChanged)
    self.cmbType.currentIndexChanged.connect(self.typeChanged)

  def valueChanged(self):
    self.model["value"] = self.txt_value.text()

  def nameChanged(self):
    self.model["name"] = self.txt_name.text()

  def typeChanged(self):
    self.model["type"] = self.cmbType.currentText()

