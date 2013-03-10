
from PySide import QtGui
from gen.resource_dialog import Ui_ResourceDialog
import os
from global_vars import GlobalVars
from confirm_dialog import ConfirmDialog
import shutil
import random
import string
class ResourceDialog(QtGui.QDialog, Ui_ResourceDialog):
  def __init__(self, root_dir, *args, **kwargs):
    super(ResourceDialog, self).__init__(*args, **kwargs)
    self.edited_resource = None
    self.model = None
    self.setupUi()
    self.bindUi()
    self.root_dir = root_dir
    self.model = {
                  "rid":None,
                  "url":None
                  }

  def setupUi(self):
    super(ResourceDialog, self).setupUi(self)

  def setModel(self, model):
    self.model = model
    self.txtName.setText(self.model["rid"])
    self.display_resource()
  
  def display_resource(self):
    self.scene = QtGui.QGraphicsScene()
    self.gvView.setScene(self.scene)
    resource_path = None
    if self.edited_resource:
      resource_path = self.edited_resource["url"]
    else:
      resource_path = os.path.join(self.root_dir, self.model["url"])
    item  = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(resource_path))
    self.scene.addItem(item)
    
  def bindUi(self):
    self.txtName.textEdited.connect(self.ridEdited)
    self.btnChange.clicked.connect(self.change_clicked)
    self.btnSave.clicked.connect(self.save_clicked)
    self.btnCancel.clicked.connect(self.cancel_clicked)
  
  def save_clicked(self):
    print 'save clicked'
    if self.edited_resource:
      self.cd = ConfirmDialog("Are you sure you want to save this Resource")
      self.cd.accepted.connect(self.on_confirmed)
      self.cd.rejected.connect(self.on_rejected)
      self.cd.show()
    else:
      self.done(0)
  
  def on_confirmed(self):
    if self.edited_resource and self.edited_resource["url"][0]!='.':
      dest=None
      if self.model["url"]:
        dest = self.model["url"]
      else:
        dest = './Resources/'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(15))
      if not os.path.exists(os.path.dirname(os.path.join(self.root_dir, dest))):
        os.makedirs(os.path.dirname(os.path.join(self.root_dir, dest)))
      shutil.copy(self.edited_resource["url"], os.path.join(self.root_dir, dest))
      self.edited_resource["url"]=dest
    self.done(1)
    

  def on_rejected(self):
    pass  
  
  def cancel_clicked(self):
    print 'edit canceled'
    self.done(0)
  
  def change_clicked(self):
    self.fo_di = QtGui.QFileDialog()
    self.fo_di.fileSelected.connect(self.file_selected)
    self.fo_di.show()
  
  def ridEdited(self, text):
    if not self.edited_resource:
      self.edited_resource = self.model.copy()
    self.edited_resource["rid"] = text
      
  def file_selected(self, f):
    if not self.edited_resource:
      self.edited_resource = self.model.copy()
      
    self.edited_resource["url"] = f
    self.display_resource()
    print "file_accepted"
     
  def get_dict(self):
    if self.edited_resource:
      return self.edited_resource


