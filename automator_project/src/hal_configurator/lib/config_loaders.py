'''
Created on Nov 19, 2012

@author: kostamihajlov
Prebuild Configuration Loaders
'''
import json
import os
from branded_apps_service import BrandedAppService as BAS
last_config_loaded = None

class ConfigLoader(object):
  def __init__(self, *args, **kwargs):
    self.custom_bundles = []
    self.custom_vars = []
  
  def loadConfig(self):
    raise NotImplementedError("abstract class accessed")
  
  def load_custom_bundles(self, config):
    config["Content"]["OperationBundles"].extend(self.custom_bundles)
    return config
  
  def load_custom_vars(self, config):
    variables = config["Variables"]
    existing_ones = [x for x in variables if len([y for y in self.custom_vars if y["name"]==x["name"]])>0]
    for k in existing_ones:
      variables.remove(k)
    variables.extend(self.custom_vars)
    return config

  def append_bundles(self, *bundles):
    self.custom_bundles.extend(bundles)
  
  def append_vars(self, *custom_vars):
    self.custom_vars.extend(custom_vars)
  
  def load_customizations(self, cfg):
    cfg = self.load_custom_bundles(cfg)
    cfg = self.load_custom_vars(cfg)
    cfg = self.fix_bundle_separator_chars(cfg)
    
    return cfg
  def fix_bundle_separator_chars(self, config):
    if os.path.sep!='/':
      for b in config["Content"]["OperationBundles"]:
        for op in b["Operations"]:
          for key in op["Arguments"].keys():
            if "Destination" in key or "File" in key:
              op["Arguments"][key]  = op["Arguments"][key].replace('/', os.pathsep)
    return config
  
class SvcConfigLoader(ConfigLoader):
  def __init__(self, svcUrl, configId):
    super(SvcConfigLoader, self).__init__()
    self.svcUrl = svcUrl
    self.__svc__ = BAS(svcUrl)
    
  def load_config(self):
    global last_config_loaded
    cfg = self.__svc__.config(self.config_id)
    last_config_loaded = cfg
    return cfg
      

class FileConfigLoader(ConfigLoader):
  def __init__(self, fileName):
    super(FileConfigLoader, self).__init__()
    self.fileName = fileName
    self.workingPath = os.path.dirname(self.fileName)
    
  def load_config(self):
    global last_config_loaded
    print os.path.abspath(self.fileName)                        
    cfg =  json.load(open(self.fileName, 'r'))
    cfg = self.load_customizations(cfg)
    cfg = self.fix_resource_separator_chars(cfg)
    last_config_loaded = cfg
    return cfg
  
  def fix_resource_separator_chars(self, config):
    if os.path.sep!='/':
      for k in config["Resources"]:
        k["url"]=k["url"].replace('/', os.pathsep)
    return config

                 
      
        

