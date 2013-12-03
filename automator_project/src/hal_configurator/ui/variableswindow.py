from PySide import QtGui, QtCore
from hal_configurator.ui.gen.variableswindow import Ui_VariablesWindow
from confirm_dialog import ConfirmDialog
from variable_dialog import VariableDialog

class VariablesWindow(QtGui.QWidget, Ui_VariablesWindow):
  def __init__(self, *args, **kwargs):
    super(VariablesWindow, self).__init__(*args, **kwargs)
    self.parent = kwargs.has_key('parent') and kwargs['parent'] or None
    self.setupUi(self)
    self.lv_items.installEventFilter(self)
    self.details_parent = None

  def setMode(self, mode):
    if not mode in ['admin', 'moderator']:
      self.btn_add.hide()
      self.btn_delete.hide()

  def setModel(self, data_model):
    self.data_model = data_model
    self.lv_items.setModel(data_model)
    self.lv_items.doubleClicked.connect(self.__on_variable_edit)
    self.btn_add.clicked.connect(self.__on_add_clicked)
    self.btn_delete.clicked.connect(self.__on_remove_clicked)

  def setDetailsContainer(self, container):
    self.details_parent = container


  def eventFilter(self, sender, event):
    if event.type() == QtCore.QEvent.KeyPress and event.matches(QtGui.QKeySequence.InsertParagraphSeparator) and sender == self.lv_items:
      self.__on_variable_edit()
    elif event.type() == QtCore.QEvent.KeyPress and event.matches(QtGui.QKeySequence.Delete) and sender == self.lv_items:
      self.__on_remove_clicked()
    elif event.type() == QtCore.QEvent.KeyPress and event.matches(QtGui.QKeySequence.New) and sender == self.lv_items:
      self.__on_add_clicked()
    else:
      return super(VariablesWindow, self).eventFilter(sender, event)

  def __on_add_clicked(self):
    self.edit_index = None
    parent = self.details_parent or QtGui.QDialog()
    self.new_dlg = VariableDialog(parent)
    self.new_dlg.setModel({"name":"", "value":"", "type":"text"})
    self.new_dlg.show()
    self.new_dlg.accepted.connect(self.__on_add_accepted)
    self.new_dlg.rejected.connect(self.__on_add_rejected)

  def __on_variable_edit(self):
    self.edit_index = self.lv_items.currentIndex()
    obj = self.data_model.data(self.edit_index, QtCore.Qt.EditRole)
    parent = self.details_parent or QtGui.QDialog()
    self.new_dlg = VariableDialog(parent)
    if not isinstance(parent,  QtGui.QDialog):
      parent.children()[0].addWidget(self.new_dlg)

    self.new_dlg.setModel(obj)
    self.new_dlg.show()
    self.new_dlg.accepted.connect(self.__on_add_accepted)
    self.new_dlg.rejected.connect(self.__on_add_rejected)

  def __on_add_accepted(self):
    variable = self.new_dlg.model
    if self.edit_index==None:
      self.data_model.appendData(variable)
    else:
      self.data_model.setData(self.edit_index, variable)

  def __on_add_rejected(self):
    "print rejected"

  def __on_remove_clicked(self):
    self.dialog = ConfirmDialog("Are you sure you want to delete this item")
    self.dialog.accepted.connect(self.__on_remove_confirmed)
    self.dialog.rejected.connect(self.__on_remove_rejected)
    self.dialog.show()


  def __on_remove_confirmed(self):
    print "remove clicked"
    print "will remove selected resource when implemented"
    print "selected resource is "+str(self.lv_items.currentIndex().row())
    self.data_model.removeData(self.lv_items.currentIndex().row())

  def __on_remove_rejected(self):
    print "remove cancelled"