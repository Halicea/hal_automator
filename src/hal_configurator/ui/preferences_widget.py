
from PySide import QtGui, QtCore
from hal_configurator.ui.gen.preferences_widget import Ui_PreferencesWidget

class PreferencesWidget(QtGui.QWidget, Ui_PreferencesWidget):

  def __init__(self,*args, **kwargs):
    super(PreferencesWidget, self).__init__(*args, **kwargs)

  def setupUi(self):
    pass
  
  def bindUi(self):
    pass