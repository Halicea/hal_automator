'''
Created on Dec 23, 2012

@author: kostamihajlov
'''
from dragable_list import DragableList
from PySide import QtGui, QtCore
import os
from ui.global_vars import GlobalVars

class ResourcesList(DragableList):
  def __init__(self, *args, **kwargs):
    super(ResourcesList, self).__init__(*args, **kwargs)
  def set_resource_root(self, resource_root):
    self.resource_root = resource_root
    
  def get_pixmap(self,index):
    
    pixmap = QtGui.QPixmap()
    img = QtGui.QImage()
    model = self.model()
    resource = model.data(index, "object")
    try:
      root_dir = os.path.dirname(GlobalVars.get_instance().current_config_path)
      img.load(os.path.join(root_dir,resource["url"]))
      pixmap.fromImage(img)
    except Exception, ex:
      print ex.message
    return pixmap
  