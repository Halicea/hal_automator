from PySide import QtGui, QtCore
from gen.variableswindow import Ui_VariablesWindow
from confirm_dialog import ConfirmDialog
from variable_dialog import VariableDialog

class VariablesWindow(QtGui.QWidget, Ui_VariablesWindow):
  def __init__(self, *args, **kwargs):
    super(VariablesWindow, self).__init__(*args, **kwargs)
    self.setupUi(self)
    self.lv_items.installEventFilter(self)
  
  def setModel(self, data_model):
    self.data_model = data_model
    self.lv_items.setModel(data_model)
    self.lv_items.doubleClicked.connect(self.__on_variable_edit)
    self.btn_add.clicked.connect(self.__on_add_clicked)
    self.btn_delete.clicked.connect(self.__on_remove_clicked)

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
    self.new_dlg = VariableDialog()
    self.new_dlg.setModel({"name":"", "value":"", "type":"text"})
    self.new_dlg.show()
    self.new_dlg.accepted.connect(self.__on_add_accepted)
    self.new_dlg.rejected.connect(self.__on_add_rejected)

  def __on_variable_edit(self):
    self.edit_index = self.lv_items.currentIndex()
    self.new_dlg = VariableDialog()
    obj = self.data_model.data(self.edit_index, QtCore.Qt.EditRole)
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