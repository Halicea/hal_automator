from PySide import QtGui, QtCore
from gen.config_bundle import Ui_BundleWidget
from config_operation import OperationWidget
from uiutils import layout_widgets
from confirm_dialog import ConfirmDialog
import hal_configurator.plugins as pl
import hal_configurator.lib.operation_factory as op_factory

from models import ToolsListModel
class OpChooserDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(OpChooserDialog, self).__init__(parent)
        self.setWindowTitle("Choose Operation Type")
        self.cmb = QtGui.QComboBox(self)
        self.cmb.setModel(ToolsListModel(pl.__all__))

class BundleWidget(QtGui.QWidget, Ui_BundleWidget):
  def __init__(self, bundle, *args, **kwargs):
    super(BundleWidget, self).__init__(*args, **kwargs)
    self.bundle= bundle
    self.ops = []
    self.setupUi()
    self.bindUi()

  def setupUi(self):
    super(BundleWidget, self).setupUi(self)
    self.delete_confirmation = ConfirmDialog("Are You sure you want to delete this operation?")
    self.delete_confirmation.accepted.connect(self.on_delete_accepted)
    self.delete_confirmation.rejected.connect(self.on_delete_rejected)
    self.btn_add_operation.clicked.connect(self.add_clicked)
    
  def bindUi(self):
    #self.la_name.setText(self.bundle["Name"])
    for op in self.bundle["Operations"]:
      self.add_operation(op)
  
  def add_clicked(self):
    b = self.op_chooser = OpChooserDialog()
    b.show()
    def on_code_chosen():
      model = b.cmb.model()
      op = model.data(model.createIndex(b.cmb.currentIndex(), 0), role = QtCore.Qt.UserRole)
      print op
      b.deleteLater()
      self.add_operation(op.get_empty_dict())
    b.cmb.currentIndexChanged.connect(on_code_chosen)
    b.show()
  
  def on_delete_accepted(self):
    l = [x for x in self.ops if x == self.op_to_delete ]
    if len(l)>0:
      print "removing"
      self.ops.remove(self.op_to_delete)
    self.op_to_delete.deleteLater();
  
  def on_delete_rejected(self):
    self.op_to_delete = None
    
  def delete_clicked(self):
    self.op_to_delete = self.sender().parent().parent();
    self.delete_confirmation.show()

  def add_operation(self, op):
    op = OperationWidget(op, self)
    op.btn_delete.clicked.connect(self.delete_clicked)
    self.ops.append(op)
    self.ltv_operations.addWidget(op)
  
  def get_dict(self):
    res = {}
    res["Name"] = self.bundle["Name"]
    ops = res["Operations"] = []
    for op in self.ops:
      ops.append(op.get_dict())
    return res
    