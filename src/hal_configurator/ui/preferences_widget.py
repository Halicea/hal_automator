
from PySide import QtGui, QtCore
from hal_configurator.ui.gen.preferences_widget import Ui_PreferencesWidget

class PreferencesWidget(QtGui.QWidget, Ui_PreferencesWidget):

  def __init__(self,*args, **kwargs):
    super(PreferencesWidget, self).__init__(*args, **kwargs)
    self.setupUi()
    self.bindUi()

  def setupUi(self):
    super(PreferencesWidget, self).setupUi(self)

  def bindUi(self):
    self.loadConfigPlugins()
    self.loadWSInfo()
    self.loadWSPlugins()

  @QtCore.Slot()
  def selectionChanged(self, item, i):
    index_map = [(0, 0, 0), (1, 0, 1), (1, 1, 2)]
    root = self.tree_sections.indexOfTopLevelItem(item)
    if(root==-1):
      root = self.tree_sections.indexOfTopLevelItem(item.parent())
    else:
      root = -1
    index = self.tree_sections.indexFromItem(item)
    print root, index.column()
    view_index = [x[2] for x in index_map if x[0] == root and x[1] == index.row()]
    if len(view_index)>0:
      self.widgets.setCurrentIndex(view_index[0])
  @QtCore.Slot()
  def loadConfigPlugins(self):
    print('saved config')
  @QtCore.Slot()
  def saveConfigPlugins(self):
    print('saved config')

  @QtCore.Slot()
  def loadWSInfo(self):
    print('loaded ws')
  @QtCore.Slot()
  def saveWSInfo(self):
    print('saved WS')

  @QtCore.Slot()
  def loadWSPlugins(self):
    print ('loaded ws plugins' )
  @QtCore.Slot()
  def saveWSPlugins(self):
    print ('saved ws plugins' )