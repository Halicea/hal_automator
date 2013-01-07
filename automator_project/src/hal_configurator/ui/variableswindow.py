from PySide import QtGui, QtCore
from gen.variableswindow import Ui_VariablesWindow
from confirm_dialog import ConfirmDialog
from variable_dialog import Dialog

class VariablesWindow(QtGui.QWidget, Ui_VariablesWindow):
  def __init__(self, *args, **kwargs):
    super(VariablesWindow, self).__init__(*args, **kwargs)
    self.setupUi(self)
  
  def setModel(self, data_model):
    self.data_model = data_model
    self.lv_items.setModel(data_model)
    self.lv_items.doubleClicked.connect(self.__on_variable_edit)
    self.btn_add.clicked.connect(self.__on_add_clicked)
    self.btn_delete.clicked.connect(self.__on_remove_clicked)
  
  def __on_add_clicked(self):
    self.edit_index = None
    self.new_dlg = Dialog()
    self.new_dlg.show()
    self.new_dlg.accepted.connect(self.__on_add_accepted)
    self.new_dlg.rejected.connect(self.__on_add_rejected)

  def __on_variable_edit(self):
    self.edit_index = self.lv_items.currentIndex()
    self.new_dlg = Dialog()
    obj = self.data_model.data(self.edit_index, QtCore.Qt.EditRole)
    self.new_dlg.txt_name.setText(obj["name"])
    self.new_dlg.txt_value.setText(obj["value"])
    self.new_dlg.show()
    self.new_dlg.accepted.connect(self.__on_add_accepted)
    self.new_dlg.rejected.connect(self.__on_add_rejected) 
  
  def __on_add_accepted(self):
    variable = self.new_dlg.get_variable()
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