'''
Created on Nov 23, 2012

@author: kostamihajlov
'''

from PySide import QtCore, QtGui
from confirm_dialog import ConfirmDialog
from hal_configurator.ui.gen.resourceswindow import Ui_ResourcesWindow
from resource_dialog import ResourceDialog

class ResourcesWindow(QtGui.QWidget, Ui_ResourcesWindow):
  def __init__(self, root_dir, *args, **kwargs):
    super(ResourcesWindow, self).__init__(*args, **kwargs)
    self.setupUi(self)
    self.show()
    self.root_dir = root_dir

  def setModel(self, model):
    self.data_model = model
    self.lv_resources.setModel(self.data_model)
    self.lv_resources.set_resource_root(self.root_dir)
    self.lv_resources.doubleClicked.connect(self.__on_resource_edit)
    self.lv_resources.installEventFilter(self)

    #self.lv_resources.key
    self.btn_add.clicked.connect(self.on_add_clicked)
    self.btn_delete.clicked.connect(self.on_remove_clicked)

  def eventFilter(self, sender, event):
    if event.type() == QtCore.QEvent.KeyPress and \
       event.matches(QtGui.QKeySequence.InsertParagraphSeparator) and \
       sender == self.lv_resources:
      self.__on_resource_edit()
    else:
      return super(ResourcesWindow, self).eventFilter(sender, event)

  def __on_resource_edit(self):
    self.edit_index = self.lv_resources.currentIndex()
    self.new_dlg = ResourceDialog(self.root_dir)
    obj = self.data_model.data(self.edit_index, QtCore.Qt.EditRole)
    self.new_dlg.setModel(obj)    
    self.new_dlg.show()
    self.new_dlg.accepted.connect(self.__on_change_accepted)
    self.new_dlg.rejected.connect(self.__on_add_rejected) 
    
  def on_add_clicked(self):
    self.edit_index = None
    self.new_dlg = ResourceDialog(self.root_dir)
    self.new_dlg.show()
    self.new_dlg.accepted.connect(self.__on_add_accepted)
    self.new_dlg.rejected.connect(self.__on_add_rejected) 
    #seld.data_model
    pass

  def __on_add_accepted(self):
    new_res = self.new_dlg.get_dict()
    if new_res:
      self.data_model.appendData(new_res)
  
  def __on_change_accepted(self):
    new_res = self.new_dlg.get_dict()
    if new_res:
      self.data_model.setData(self.lv_resources.currentIndex(), new_res)
      
  
  def __on_add_rejected(self):
    print "add rejected"
    
  def on_remove_clicked(self):
    self.dialog = ConfirmDialog("Are you sure you want to delete this item")
    self.dialog.accepted.connect(self.on_remove_confirmed)
    self.dialog.rejected.connect(self.on_remove_rejected)
    self.dialog.show()

  def on_remove_confirmed(self):    
    print "remove clicked"
    #print "will remove selected resource when implemented"
    print "selected resource is "+str(self.lv_resources.currentIndex().row())
    self.data_model.removeData(self.lv_resources.currentIndex().row())
    
  def on_remove_rejected(self):
    print "remove cancelled"