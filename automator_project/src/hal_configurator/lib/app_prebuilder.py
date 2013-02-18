import os
import urllib2
class AppPreBuilder(object):
  def __init__(self, config_loader, executor):
    self.loader = config_loader
    self.executor = executor
    self.config = None
    #self.resources_root = resources_root
    
  def get_config(self):
    print "in configure"
    if self.config:
      print "returning config"
      return self.config
    else:
      self.config = self.loader.load_config()
      print "config loaded"
    return self.config

  def apply(self):
    print "started execution"
    old_dir = os.getcwd()
    os.chdir(self.get_execution_dir())

    cnf = self.get_config()
    self.configure(cnf)
    print "finished execution"
    os.chdir(old_dir)

  def get_execution_dir(self):
    return self._execution_dir and self._execution_dir or os.getcwd()

  def set_execution_dir(self, execution_dir):
    self._execution_dir = execution_dir

  def configure(self, cnf):
    global_vars=[]
    if cnf.has_key("Variables"):
      global_vars = cnf["Variables"]
    global_resources = []
    if cnf.has_key("Resources"):
      global_resources = cnf["Resources"]
    for k in cnf["Content"]["OperationBundles"]:
      self.executor.execute_bundle(k, global_vars, global_resources)
