from PySide import QtGui, QtCore
# from config_operation import OperationWidget
from config_operation_old import OperationWidget
from confirm_dialog import ConfirmDialog
from hal_configurator.lib.plugin_loader import get_plugins_list
from hal_configurator.ui.gen.config_bundle import Ui_BundleWidget
from models import ToolsListModel


class BundleWidget(QtGui.QWidget, Ui_BundleWidget):
  def __init__(self, bundle, *args, **kwargs):
    super(BundleWidget, self).__init__(*args, **kwargs)
    self.scroll_on = True
    self.bundle= bundle
    self.setupUi()
    self.bindUi()

  def set_vertical_scroll(self, on):
    self.scroll_on = on
    self.updateGeometry()

  def sizeHint(self):
    s = None
    if self.scroll_on:
      s = super(BundleWidget,self).sizeHint()
    else:
      s = QtCore.QSize(super(BundleWidget,self).sizeHint().width(), 50+ self.contents.sizeHint().height())
    return s

  def setupUi(self):
    super(BundleWidget, self).setupUi(self)
    self.delete_confirmation = ConfirmDialog("Are You sure you want to delete this operation?")
    self.delete_confirmation.accepted.connect(self.on_delete_accepted)
    self.delete_confirmation.rejected.connect(self.on_delete_rejected)

  def bindUi(self):
    self.contents.set_bundle(self.bundle)

  def on_delete_accepted(self):
    self.contents.remove_operation(self.op_to_delete)
      
  def on_delete_rejected(self):
    self.op_to_delete = None
    
  def delete_clicked(self):
    self.op_to_delete = self.sender()
    self.delete_confirmation.show()

  def get_dict(self):
    return self.contents.get_dict()
    
# Not in use now    
class OpChooserDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(OpChooserDialog, self).__init__(parent)
        self.setWindowTitle("Choose Operation Type")
        self.cmb = QtGui.QComboBox(self)
        self.cmb.setModel(ToolsListModel(sorted(get_plugins_list())))
    