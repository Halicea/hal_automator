
from PySide import QtGui, QtCore
from hal_configurator.ui.gen.preferences_widget import Ui_PreferencesWidget
from hal_configurator.lib.workspace_manager import Workspace
from hal_configurator.lib import app_config
from hal_configurator.lib.app_config import config

class PreferencesWidget(QtGui.QWidget, Ui_PreferencesWidget):

  def __init__(self,*args, **kwargs):
    super(PreferencesWidget, self).__init__(*args, **kwargs)
    self.setupUi()
    self.bindUi()
    self.setWindowTitle('Preferences')

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
    ctrls = [self.gen_p1,self.gen_p2,self.gen_p3,self.gen_p4,self.gen_p5]
    for i, ctrl in enumerate(ctrls):
      if i < len(config.plugin_dirs):
        ctrl.setText(config.plugin_dirs[i])
      else:
        ctrl.setText('')
    
    
  @QtCore.Slot()
  def saveConfigPlugins(self):
    ctrls = [self.gen_p1,self.gen_p2,self.gen_p3,self.gen_p4,self.gen_p5]
    plugins = []
    for i, c in enumerate(ctrls):
      plugins.append(c.text().strip())
    config.plugin_dirs = plugins
    app_config.save()
      
  
  @QtCore.Slot()
  def loadWSInfo(self):
    ws_dir = Workspace.current.workspacedir
    ws_name = Workspace.current.name
    self.ws_path.setText(ws_dir)
    self.ws_name.setText(ws_name)
    
  @QtCore.Slot()
  def saveWSInfo(self):
    ws_name = self.ws_name.text()
    Workspace.current.name = ws_name
    
  @QtCore.Slot()
  def loadWSPlugins(self):
    ctrls = [self.ws_p1,self.ws_p2,self.ws_p3,self.ws_p4,self.ws_p5]
    plugin_dirs = Workspace.current.plugin_dirs
    for i, ctrl in enumerate(ctrls):
      if i < len(plugin_dirs):
        ctrl.setText(plugin_dirs[i])
      else:
        ctrl.setText('')
    
  @QtCore.Slot()
  def saveWSPlugins(self):
    ctrls = [self.ws_p1,self.ws_p2,self.ws_p3,self.ws_p4,self.ws_p5]
    plugins =[]
    for c in ctrls:
      if c.text().strip():
        plugins.append(c.text().strip())
    Workspace.current.plugin_dirs = plugins
    Workspace.current.save()
    
    