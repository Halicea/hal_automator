from PySide import QtCore
import lib.operation_factory as fact

class ResourcesListModel(QtCore.QAbstractListModel):
  
  def __init__(self, resources, *args, **kwargs):
    super(ResourcesListModel, self).__init__(*args, **kwargs)
    self.resources = resources  
    self.setSupportedDragActions(QtCore.Qt.MoveAction)

  def rowCount(self, parent):
    return len(self.resources)

  def data(self, index, role):
    if role == QtCore.Qt.DisplayRole:
      item = self.resources[index.row()]["url"]
      return str(item)
    elif role==QtCore.Qt.UserRole:
      return self.resources[index.row()]["rid"]
    elif role=="object":
      return self.resources[index.row()]
  
  def appendData(self, item):
    self.beginInsertRows(None, len(self.resources), len(self.resources))
    self.resources.append(item)
    self.endInsertRows()
    
  def removeRows(self, index):
    self.beginInsertRows(None, len(self.resources), len(self.resources))
    del self.resources[index]
    self.endInsertRows()
      
class VariablesListModel(QtCore.QAbstractListModel):

  def __init__(self, resources, *args, **kwargs):
    super(VariablesListModel, self).__init__(*args, **kwargs)
    self.resources = resources
    self.setSupportedDragActions(QtCore.Qt.MoveAction)
  
  def rowCount(self, parent):
    return len(self.resources)

  def data(self, index, role):
    if role == QtCore.Qt.DisplayRole:
      item = '->'.join([self.resources[index.row()]["name"], self.resources[index.row()]["value"]])  
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
    
class OperationTypeListModel(QtCore.QAbstractListModel):
  
  def __init__(self, *args, **kwargs):
    super(OperationTypeListModel,self).__init__(*args, **kwargs)
 
    self.op_types = fact.get_operation_codes()
    self.op_types.insert(0, "--Select Type--")
  
  def rowCount(self, parent):
    return len(self.op_types)
    
  def data(self, index, role):
    if role == QtCore.Qt.DisplayRole:
      return self.op_types[index.row()]
    elif role == QtCore.Qt.UserRole:
      return fact.new_operation(self.op_types[index.row()])
    return None

class ObjectWrapper(QtCore.QObject):
    def __init__(self, thing):
        QtCore.QObject.__init__(self)
        self._thing = thing
 
    def _name(self):
        return str(self._thing)
      
    changed = QtCore.Signal()
    name = QtCore.Property(unicode, _name, notify=changed)



  
