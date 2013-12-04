
from PySide import QtGui, QtCore
from PySide.QtCore import Qt
from hal_configurator.ui.gen.variable_dialog import Ui_Form
from hal_configurator.ui.models import SimpleStringListModel
from hal_configurator.lib.workspace_manager import Workspace

class Communicator(QtCore.QObject):
  speak = QtCore.Signal()
  def __init__(self):
    super(Communicator, self).__init__()

class VariableDialog(QtGui.QWidget, Ui_Form):
  accepted = QtCore.Signal()
  rejected = QtCore.Signal()
  def __init__(self, *args, **kwargs):
    super(VariableDialog, self).__init__(*args, **kwargs)
    self.model = None
    if isinstance(self.parent(), QtGui.QDialog):
      self.db = self.parent()
    self.types_model = ["text", "file", "color","bool", "url", "select"]
    self.setupUi()
    self.bindUi()

  def setupUi(self):

    super(VariableDialog, self).setupUi(self)
    if Workspace.current.mode !='admin':  # @UndefinedVariable
      self.txtDisplay.setEnabled(False)
      self.adminPanel.hide()

  def show(self):
    if isinstance(self.parent(), QtGui.QDialog):
      self.parent().show()
    super(VariableDialog, self).show()

  def checkstate_from_bool(self, value):
    if value == None:
      return Qt.CheckState.PartiallyChecked
    if value:
      return Qt.CheckState.Checked
    else:
      return Qt.CheckState.Unchecked
  def checkstate_to_bool(self, value):
    if value == Qt.CheckState.Checked:
      return True
    elif value == Qt.CheckState.Unchecked:
      return False
    elif value == Qt.CheckState.PartiallyChecked:
      return None

  def setModel(self, model):
    self.model = model
    t = "text"
    if self.model.has_key("type"):
      t = self.model["type"]

    self.txt_name.setText(self.model["name"])
    self.txt_value.setText(self.model["value"])
    self.txtDisplay.setText(self.model.has_key('display') and self.model['display'] or '')
    self.cbAdminOnly.setCheckState(self.checkstate_from_bool(self.model.has_key('admin_only') and self.model['admin_only'] or None))
    self.cbRequired.setCheckState(self.checkstate_from_bool(self.model.has_key('required') and self.model['required'] or None))
    self.cmbType.setCurrentIndex(self.types_model.index(t))

  def bindUi(self):
    self.cmbType.setModel(SimpleStringListModel(self.types_model))
    self.txt_value.textChanged.connect(self.valueChanged)
    self.txt_name.textChanged.connect(self.nameChanged)
    self.cmbType.currentIndexChanged.connect(self.typeChanged)
    self.cbAdminOnly.clicked.connect(self.adminOnlyChanged)
    self.cbRequired.clicked.connect(self.requiredChanged)
    self.txtDisplay.textChanged.connect(self.displayChanged)
    self.buttonBox.accepted.connect(self.__btn_accepted__)
    self.buttonBox.rejected.connect(self.__btn_rejected__)

  def __btn_accepted__(self):
    self.accepted.emit()
    if isinstance(self.parent(), QtGui.QDialog):
      self.parent().close()
    else:
      self.close()

  def __btn_rejected__(self):
    self.rejected.emit()
    if isinstance(self.parent(), QtGui.QDialog):
      self.parent().close()
    else:
      self.close()


  def valueChanged(self):
    self.model["value"] = self.txt_value.text()

  def nameChanged(self):
    self.model["name"] = self.txt_name.text()

  def typeChanged(self):
    self.model["type"] = self.cmbType.currentText()

  def displayChanged(self):
    self.model["display"] = self.txtDisplay.text()

  def adminOnlyChanged(self):
    self.model["admin_only"]=self.checkstate_to_bool(self.cbAdminOnly.checkState())

  def requiredChanged(self):
    self.model["required"]=self.checkstate_to_bool(self.cbRequired.checkState())

