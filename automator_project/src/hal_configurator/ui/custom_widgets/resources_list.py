'''
Created on Dec 23, 2012

@author: kostamihajlov
'''
from dragable_list import DragableList
from PySide import QtGui
import os

class ResourcesList(DragableList):
  def __init__(self, *args, **kwargs):
    super(ResourcesList, self).__init__(*args, **kwargs)
    self.resource_root = "/"
  def set_resource_root(self, resource_root):
    self.resource_root = resource_root
    
  def get_pixmap(self,index):
    pixmap = QtGui.QPixmap()
    resource = self.model().data(index, "object")
    try:
      img_path = os.path.join(self.resource_root,resource["url"])
      if not pixmap.load(img_path):
        super(ResourcesList, self).get_pixmap(index)
    except Exception, ex:
      print ex.message
    return pixmap
  