'''
Created on Nov 21, 2012

@author: kostamihajlov
'''
import os
from PySide import QtGui, QtCore
from gen.mainwindow import Ui_MainWindow
from configwindow import ConfigWindow
from lib.config_loaders import FileConfigLoader
from ui.regex_tool import RegexTool
from global_vars import GlobalVars

config_path = '/Users/kostamihajlov/MyProjects/PrintStandClient/src/Configs'
solution_dir = "/Users/kostamihajlov/MyProjects/PrintStandClient/src/{PlatformType}/Mediawire.PrintStand.Mobile.Presentation"
solution_for_platform = {"Android":"MonoDroid", "IOS":"MonoTouch"}
fpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_runner_script = os.path.join(fpath, 'lib', 'configurator_console.py')
regex_shown = False

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
  def __init__(self, *args, **kwargs):
    self.fullScreen = False
    super(MainWindow, self).__init__(*args, **kwargs)
    self.setupUi(self)
    self.show()
    self.pb_build_progress.setHidden(True)
    self.bind_controls()
    self.building = False
    self.proc = None
    self.build_step = 0
    self.working_dir = None
    self.regex_tool = None
    
  def bind_controls(self):
    self.btn_build.clicked.connect(self.on_build_clicked)
    self.cmb_brands.currentIndexChanged.connect(self.on_brand_changed)
    self.brands_model = SimpleStringListModel(self.get_available_brands())
    self.cmb_brands.setModel(self.brands_model)
    
    self.cmb_platforms.setModel(SimpleStringListModel(self.get_platforms_for_brand(None)))
    self.cmb_platforms.currentIndexChanged.connect(self.on_platform_changed)
    self.btn_configure.clicked.connect(self.on_configure_clicked)
    self.btn_show_config.clicked.connect(self.show_config_clicked)
    self.btn_install_on_device.clicked.connect(self.on_install_clicked)
    self.btn_reset_scm.clicked.connect(self.on_scm_reset_clicked)
    self.btn_sign.clicked.connect(self.on_sign_app_clicked)
    
    self.actionRegex_Tool.triggered.connect(self.toggle_regex_tool)
  
  def toggle_regex_tool(self):
    global regex_shown
    if not self.regex_tool:
      self.regex_tool = RegexTool()
    if regex_shown:
      self.regex_tool.hide()
    else:
      self.regex_tool.show()
    regex_shown = not regex_shown
    
  def get_available_brands(self):
    brands =  [d for d in os.listdir(config_path) if os.path.isdir(os.path.join(config_path, d))]
    brands.insert(0, "--Select Brand--")
    return brands
  
  def on_install_clicked(self):
    self.run_external_proc("make install", os.path.dirname(self.working_dir))
  
  def on_scm_reset_clicked(self):
    self.run_external_proc("git reset --hard HEAD", os.path.dirname(self.working_dir))
  
  def on_sign_app_clicked(self):
    self.run_external_proc("make sign", os.path.dirname(self.working_dir))
    
  def show_config_clicked(self):
    if self.working_dir:
      self.config = FileConfigLoader(self.get_config_path()).load_config()
      self.cfg = ConfigWindow(self.config)
      self.cfg.cw.set_save_path(self.get_config_path())
      self.cfg.show()
      
  def get_platforms_for_brand(self, brand):
    plats = []
    if brand:
      bpath = os.path.join(config_path, brand)
      if os.path.exists(bpath):
        plats =  [d for d in os.listdir(bpath) if os.path.isdir(os.path.join(bpath, d))]
    plats.insert(0, "--Select Platform--")
    return plats
  
  def on_brand_changed(self):
    brand = self.cmb_brands.currentText()
    self.cmb_platforms.setModel(SimpleStringListModel(self.get_platforms_for_brand(brand)))
    
  def on_platform_changed(self):
    ind = self.cmb_platforms.currentIndex()
    if ind>0:
      self.working_dir  = solution_dir.replace('{PlatformType}', solution_for_platform[self.cmb_platforms.currentText()])
    else:
      self.working_dir = None
    print self.working_dir
    
  def on_configure_clicked(self):
    self.run_external_proc(self.get_configure_command(), self.working_dir)
    
  def on_build_clicked(self):
    if self.working_dir:
      if self.is_repo_clean():
        self.building = not self.building
        if self.building:
          self.start_build("make build", os.path.dirname(self.working_dir))
          self.btn_build.setText("Cancel") 
          self.freeze_buttons(True)
        else:
          self.cancel_build()
          self.btn_build.setText("Build")
          self.freeze_buttons(False)
      else:
        print "repo is not commited"
    else:
      print "no working dir set"
      
  def get_config_path(self):
    vars = GlobalVars.get_instance()
    vars.current_config_path=os.path.join(config_path, self.cmb_brands.currentText(), self.cmb_platforms.currentText(),"bc.json")      
    return vars.current_config_path
  
    #self.pb_build_progress.setHidden(not self.building)
  def get_configure_command(self):
    runner = config_runner_script
    runner_config= self.get_config_path()
    cmd =  "python "+runner+" -from fs "+runner_config
    if self.cb_verbose.isChecked():
      cmd+=" -v"
    return cmd
  
  def is_repo_clean(self):
    #self.start_build("git status", self.working_dir)
    return True
  
  def start_build(self, comm, working_dir):
    self.build_step+=1
    print working_dir
    print "building"
    self.proc = QtCore.QProcess(self)
    self.proc.setWorkingDirectory(working_dir)
    self.proc.readyReadStandardOutput.connect(self.__show_output__)
    self.proc.readyReadStandardOutput.connect(self.__show_error__)
    self.proc.setProcessChannelMode(QtCore.QProcess.ProcessChannelMode.MergedChannels)
    self.proc.closeWriteChannel()
    self.proc.stateChanged.connect(self.__build_state_changed__)
    #self.proc.setReadChannel(QtCore.QProcess.StandardError)
    self.proc.start(comm)
    
    #self.proc.start("make", "configure brand="++" verbose=-v")

  def run_external_proc(self, cmd,working_dir):
    self.proc = QtCore.QProcess(self)
    self.proc.setWorkingDirectory(working_dir)
    self.proc.readyReadStandardOutput.connect(self.__show_output__)
    self.proc.readyReadStandardOutput.connect(self.__show_error__)
    self.proc.setProcessChannelMode(QtCore.QProcess.ProcessChannelMode.MergedChannels)
    self.proc.closeWriteChannel()
    #self.proc.setReadChannel(QtCore.QProcess.StandardError)
    self.proc.start(cmd)
    #self.proc.start("make", "configure brand="++" verbose=-v")

  def __show_output__(self):
    output = self.proc.readAllStandardOutput()
    self.txt_output.append(str(output))
    
  def __show_error__(self):
    output = self.proc.readAllStandardError()
    self.txt_output.append(str(output))
  
  def __build_state_changed__(self, st):
    if st== QtCore.QProcess.ProcessState.NotRunning:  
      if self.build_step == 1:
        if self.cb_revert.isChecked():
          print "Reverting changes"
          self.start_build("git reset --hard HEAD", self.working_dir)
        else:
          print "Skipped Reverting"
          self.build_step+=1
          
      if self.build_step == 2:
        self.btn_build.setText("Build Again")
        self.freeze_buttons(False)
        self.building = False
        self.build_step = -1
    #if  QtCore.QProcess.ProcessState. 
    
  def cancel_build(self):
    print "cancelled"
    self.txt_output.clear()
    
  def freeze_buttons(self, freeze):
    self.cmb_brands.setDisabled(freeze)
    self.cmb_platforms.setDisabled(freeze)
    #self.cb_verbose.setDisabled(freeze)
  
class SimpleStringListModel(QtCore.QAbstractListModel):
  
  def __init__(self, data):
    super(SimpleStringListModel, self).__init__()
    self.__data__ = data

  def rowCount(self, *args, **kwargs):
    return len(self.__data__)

  def data(self, index, parent):
    return str(self.__data__[index.row()])


    
    