import os

from PySide import QtGui
from PySide.QtCore import QThread

from hal_configurator.lib import app_config
from hal_configurator.ui.console_output import ConsoleOutput
from hal_configurator.lib.app_prebuilder import AppConfigurator
from hal_configurator.lib.config_loaders import FileConfigLoader
from gen.configwindow import Ui_ConfigWindow
from config_widget import ConfigForm
from hal_configurator.lib.logers import ZmqChainedLoger
from hal_configurator.ui.config_runner_thread import ConfigRunnerThread
from hal_configurator.ui.message_subscriber import MessageSubsriberThread
from hal_configurator.ui.models import ToolsListModel
from hal_configurator.lib.app_config import config
from hal_configurator.lib.plugin_loader import get_plugins

class ConfigWindow(QtGui.QMainWindow, Ui_ConfigWindow):


  def __init__(self, main_window, config_path, working_dir, *args, **kwargs):

    super(ConfigWindow, self).__init__(*args, **kwargs)
    self.config_path = config_path
    if working_dir:
      self.working_dir = working_dir
    else:
      self.working_dir = app_config.get_working_dir()

    self.configuration = FileConfigLoader(self.config_path).load_config()
    self.main_window = main_window
    self.working_dir_choser = None
    self.cw = None
    self.set_plugins()
    self.setupUi()
    self.bindUi()
    self.set_menu_bar()

  def set_plugins(self):
    self.plugins =[]
    for d in config.plugin_dirs:
      self.plugins.extend(get_plugins(d))

  def setupUi(self):
    super(ConfigWindow, self).setupUi(self)
    #layout = QtGui.QVBoxLayout()
    #layout.addWidget(self.cw)

  def focusInEvent(self, *args, **kwargs):
    self.main_window.set_config_menu()
    self.bindUi()

  def bindUi(self):
    title = os.path.basename((os.path.dirname(os.path.dirname(self.config_path))))
    self.setWindowTitle(title)
    self.cw = ConfigForm(self.configuration, self.config_path)
    self.ltv_content.addWidget(self.cw)
    self.tool = QtGui.QListView(self)
    self.tool.setModel(ToolsListModel(self.plugins, False))
    self.lv_tools.addWidget(self.tool)
    self.splitter.setSizes([self.splitter.height(), 0])
    self.splitter_2.setSizes([self.splitter_2.width(), 0])
    self.btnRun.clicked.connect(self.on_run_click)
    self.txtWorkingDir.setText(self.working_dir)
    self.cbChooseWorkingDir.clicked.connect(self.chose_working_dir)
    self.menubar.setWindowTitle(title)
    self.build_output = None

  def chose_working_dir(self):
    """
    Choses the current working directory for the current configuration

    """
    res = QtGui.QFileDialog.getExistingDirectory(caption="Choose working directory")
    if res:
      app_config.set_working_dir(res)
      self.working_dir = res
      self.txtWorkingDir.setText(res)

  def set_menu_bar(self):
    self.actionSave.triggered.connect(self.cw.save_config)
    self.actionRun.triggered.connect(self.on_run_click)
    self.actionClone.triggered.connect(self.clone_config)
    self.actionClose.triggered.connect(self.close)

  def on_run_click(self):
    root_url = os.path.dirname(self.config_path)
    if os.name!='posix':
      root_url = '/'+root_url
    if self.build_output:
      self.build_output.close()
    self.build_output = ConsoleOutput()
    self.build_output.show()
    config_loader = FileConfigLoader(self.config_path)
    builder = AppConfigurator(config_loader, ZmqChainedLoger(1234))
    builder.set_execution_dir(self.working_dir)
    self.worker = ConfigRunnerThread(builder)
    self.set_message_receiver()
    self.worker.start()
    self.worker.finished.connect(self.on_worker_finished)

  def on_worker_finished(self):
    self.worker.builder = None
    del self.worker
    self.messages_thread.terminate()
    del self.messages_thread

  def set_message_receiver(self):
    self.messages_thread = MessageSubsriberThread(1234)
    self.messages_thread.on_message_received.connect(self.on_message_received)
    self.messages_thread.start(QThread.TimeCriticalPriority)

  def on_message_received(self, message):
    self.build_output.txt_output.append("%s" % message)

  def clone_config(self):
    print "just cloned"
