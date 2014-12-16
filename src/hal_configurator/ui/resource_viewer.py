
from PySide import QtGui
from hal_configurator.ui.gen.resource_viewer import Ui_ResourceViewer

class ResourceViewer(QtGui.QWidget, Ui_ResourceViewer):
  def __init__(self, *args, **kwargs):
    super(ResourceViewer, self).__init__(*args, **kwargs)
    self.setupUi()
    self.bindUi()

  def setupUi(self):
    super(ResourceViewer, self).setupUi(self)

  def bindUi(self):
    pass
