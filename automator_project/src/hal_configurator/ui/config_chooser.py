
from PySide import QtGui
from gen.config_chooser import Ui_ConfigChooserWidget
from hal_configurator.lib.config_loaders import FileConfigLoader
from hal_configurator.ui.configwindow import ConfigWindow

class ConfigChooserWidget(QtGui.QWidget, Ui_ConfigChooserWidget):
  def __init__(self, *args, **kwargs):
    super(ConfigChooserWidget, self).__init__(*args, **kwargs)
    self.setupUi()
    self.bindUi()

  def setupUi(self):
    super(ConfigChooserWidget, self).setupUi(self)

  def bindUi(self):
    self.btn_open_config.clicked.connect(self.open_clicked)
    
  def open_clicked(self):
    fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '~')
    config = FileConfigLoader(fname).load_config()
    self.cf = ConfigWindow(config)
    self.cf.show()
