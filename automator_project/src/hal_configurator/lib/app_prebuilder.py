import os
import urllib2
class AppPreBuilder(object):
  def __init__(self, config_loader, executor):
    self.loader = config_loader
    self.executor = executor
    self.config = None
    #self.resources_root = resources_root
    
  def get_config(self):
    if self.config:
      return self.config
    else:
      self.config = self.loader.load_config()
    return self.config

  def apply(self):
    cnf = self.get_config()
    self.configure(cnf)

  def configure(self, cnf):
    global_vars=[]
    if cnf.has_key("Variables"):
      global_vars = cnf["Variables"]
    global_resources = []
    if cnf.has_key("Resources"):
      global_resources = cnf["Resources"]
    for k in cnf["Content"]["OperationBundles"]:
      print "ok"
      self.executor.execute_bundle(k, global_vars, global_resources)
