from dragable_list import DragableList
from PySide import QtGui, QtCore
from hal_configurator.ui.models import ToolsListModel
from hal_configurator.lib.plugin_loader import get_plugins_list
import os

class PluginsList(DragableList):
  
  def __init__(self, *args, **kwargs):
    super(PluginsList, self).__init__(*args, **kwargs)
    self.object_format = 'application/x-plugin'
    items = sorted(get_plugins_list())
    self.main_model = ToolsListModel(items, include_void=False)
    self.proxyModel =  QtGui.QSortFilterProxyModel(self)
    self.proxyModel.setSourceModel(self.main_model)
    self.setModel(self.proxyModel)
  
  @QtCore.Slot(str)
  def filter(self, text):
    print 'Searching:', text
    self.proxyModel.setFilterWildcard(text)
    self.proxyModel.setFilterKeyColumn(0)
  

