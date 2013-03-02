from PySide import QtCore, QtGui
import hal_configurator.lib.operation_factory as fact
import os
from global_vars import GlobalVars
import hal_configurator.plugins as plugins
class ResourcesListModel(QtCore.QAbstractListModel):
  
  def __init__(self, resources, root_dir,  *args, **kwargs):
    super(ResourcesListModel, self).__init__(*args, **kwargs)
    self.resources = resources  
    self.setSupportedDragActions(QtCore.Qt.MoveAction)
    self.root_dir = root_dir
  
  def rowCount(self, parent):
    return len(self.resources)

  def data(self, index, role):
    if role == QtCore.Qt.DisplayRole:
      item = self.resources[index.row()]["rid"]
      return str(item)
    elif role==QtCore.Qt.UserRole:
      return "{#"+self.resources[index.row()]["rid"]+"#}"
    elif role==QtCore.Qt.EditRole:
      return self.resources[index.row()]
    elif role=="object":
      return self.resources[index.row()]
  
  def appendData(self, item):
    self.beginInsertRows(QtCore.QModelIndex(), len(self.resources), len(self.resources))
    self.resources.append(item)
    self.endInsertRows()
  
  def removeData(self, index):
    self.beginRemoveRows(QtCore.QModelIndex(), index, index)
    to_remove = os.path.join(self.root_dir, self.resources[index]["url"])
    print "To Remove", to_remove
    if(os.path.exists(os.path.join(self.root_dir, self.resources[index]["url"]))):
      os.remove(os.path.join(self.root_dir, self.resources[index]["url"]))
    del self.resources[index]
    self.endRemoveRows()    
  
  def removeRows(self, index):
    self.beginInsertRows(None, len(self.resources), len(self.resources))
    del self.resources[index]
    self.endInsertRows()
  
  def setData(self, index, value):
    self.resources[index.row()] = value
    return True
      
class VariablesListModel(QtCore.QAbstractListModel):

  def __init__(self, resources, *args, **kwargs):
    super(VariablesListModel, self).__init__(*args, **kwargs)
    self.resources = resources
    self.setSupportedDragActions(QtCore.Qt.MoveAction)
  
  def rowCount(self, parent):
    return len(self.resources)

  def data(self, index, role):
    if role == QtCore.Qt.DisplayRole:
      item = self.resources[index.row()]["name"]  
      return str(item)
    elif role == QtCore.Qt.UserRole:
      return "{{"+self.resources[index.row()]["name"]+"}}"
    elif role == QtCore.Qt.EditRole:
      return  self.resources[index.row()]
  
  def appendData(self, item):
    self.beginInsertRows(QtCore.QModelIndex(), len(self.resources), len(self.resources))
    self.resources.append(item)
    self.endInsertRows()
    
  def removeData(self, index):
    self.beginRemoveRows(QtCore.QModelIndex(), index, index)
    
    del self.resources[index]
    
    self.endRemoveRows()
  
  def setData(self, index, value):
    self.resources[index.row()] = value
    return True
    
# class OperationTypeListModel(QtCore.QAbstractListModel):
#
#   def __init__(self, *args, **kwargs):
#     super(OperationTypeListModel,self).__init__(*args, **kwargs)
#
#     self.op_types = fact.get_operation_codes()
#     self.op_types.insert(0, "--Select Type--")
#
#   def rowCount(self, parent):
#     return len(self.op_types)
#
#   def data(self, index, role):
#     if role == QtCore.Qt.DisplayRole:
#       return self.op_types[index.row()]
#     elif role == QtCore.Qt.UserRole:
#       return fact.new_operation(self.op_types[index.row()])
#     return None


class ToolsListModel(QtCore.QAbstractListModel):
  def __init__(self, tools, include_void=True, *args, **kwargs):
    super(ToolsListModel,self).__init__(*args, **kwargs)
    self.tools = tools
    if include_void:
      self.tools.insert(0, '--Select Item--')

  def rowCount(self, parent):
    return len(self.tools)
    
  def data(self, index, role):
    if role == QtCore.Qt.DisplayRole:
      return self.tools[index.row()]
      #plugin_cls = plugins.__dict__[tool]
      #b.setText(plugin_cls.get_name())
      #return b
    elif role == QtCore.Qt.UserRole:
      return plugins.__dict__[self.tools[index.row()]]
      #return fact.new_operation(self.tools[index.row()])
    return None
  
class ObjectWrapper(QtCore.QObject):
    def __init__(self, thing):
        QtCore.QObject.__init__(self)
        self._thing = thing
        
    def _name(self):
        return str(self._thing)
      
    changed = QtCore.Signal()
    name = QtCore.Property(unicode, _name, notify=changed)


class SimpleStringListModel(QtCore.QAbstractListModel):
  def __init__(self, data):
    super(SimpleStringListModel, self).__init__()
    self.__data__ = data

  def rowCount(self, *args, **kwargs):
    return len(self.__data__)

  def data(self, index, parent):
    return str(self.__data__[index.row()])