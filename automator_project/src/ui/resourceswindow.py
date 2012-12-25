'''
Created on Nov 23, 2012

@author: kostamihajlov
'''

from gen.resourceswindow import Ui_ResourcesWindow
from PySide import QtCore, QtGui
from ui.confirm_dialog import ConfirmDialog

class ResourcesWindow(QtGui.QWidget, Ui_ResourcesWindow):
  def __init__(self,*args, **kwargs):
    super(ResourcesWindow, self).__init__(*args, **kwargs)
    self.setupUi(self)
    self.show()

  def setModel(self, model):
    self.data_model = model
    self.lv_resources.setModel(self.data_model)
    self.btn_add.clicked.connect(self.on_add_clicked)
    self.btn_delete.clicked.connect(self.on_remove_clicked)
  
  def on_add_clicked(self):
    #resource = self.dialog.get_resource()
    #seld.data_model
    pass
  
  def on_remove_clicked(self):
    self.dialog = ConfirmDialog("Are you sure you want to delete this item")
    self.dialog.accepted.connect(self.on_remove_confirmed)
    self.dialog.rejected.connect(self.on_remove_rejected)
    self.dialog.show()

  def on_remove_confirmed(self):    
    print "remove clicked"
    print "will remove selected resource when implemented"
    print "selected resource is "+str(self.lv_resources.currentIndex().row())
    
  def on_remove_rejected(self):
    print "remove cancelled"
    
  
    
