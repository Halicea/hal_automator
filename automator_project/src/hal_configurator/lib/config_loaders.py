'''
Created on Nov 19, 2012

@author: kostamihajlov
Prebuild Configuration Loaders
'''
import json
import os
import urllib
from app_config import config
import shutil
from branded_apps_service import BrandedAppService as BAS
last_config_loaded = None


class ConfigLoader(object):
  def __init__(self, *args, **kwargs):
    self.custom_bundles = []
    self.custom_vars = []
    self.resources_root_url = None

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
  
  def verify_required_vars(self, config):
    variables = config["Variables"]
    required = config["RequiredVariables"]
    for rv in required:
      v = [x for x in variables if x["name"] == rv["name"]]
      if not v:
        variables.insert(0, rv)
      else:
        if len(v)==1:
          v = v[0]
        else:
          raise Exception('Variable %s is defined % times, it should be only once.'%(rv['name'], len(v)))
        for key in rv:
          if key!='name' and key!='value':
            if rv[key]!=None and rv[key]!='':
              v[key] = rv[key]
        v['is_from_req'] = True
    return  config

  def append_bundles(self, *bundles):
    self.custom_bundles.extend(bundles)
  
  def append_vars(self, *custom_vars):
    self.custom_vars.extend(custom_vars)
  
  def load_customizations(self, cfg):
    cfg = self.load_custom_bundles(cfg)
    cfg = self.load_custom_vars(cfg)
    #cfg = self.fix_bundle_separator_chars(cfg)
    cfg = self.verify_required_vars(cfg)
    return cfg

  # def fix_bundle_separator_chars(self, config):
  #   if os.path.sep!='/':
  #     for b in config["Content"]["OperationBundles"]:
  #       for op in b["Operations"]:
  #         for key in op["Arguments"].keys():
  #           if "Destination" in key or "File" in key:
  #             op["Arguments"][key]  = op["Arguments"][key].replace('/', os.sep)
  #   return config
  
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
    self.config_file = fileName
    self.resources_root = os.path.abspath(os.path.dirname(self.config_file))
    self.resource_root_url = urllib.pathname2url(self.resources_root)

  def load_config(self):
    global last_config_loaded
    print os.path.abspath(self.config_file)
    cfg =  json.load(open(self.config_file, 'r'))
    if cfg["Content"].has_key("Reference"):
      content_path = os.path.join(os.path.dirname(self.config_file), cfg["Content"]["Reference"])
      content = json.load(open(content_path , "r"))
      content["Reference"] = cfg["Content"]["Reference"]
      cfg["Content"] = content

    if "RequiredVariables" in cfg:
      if cfg["RequiredVariables"].has_key("Reference"):
        content_path = os.path.join(os.path.dirname(self.config_file), cfg["RequiredVariables"]["Reference"])
        content = json.load(open(content_path, "r"))
        cfg["RequiredVariables-Reference"] = cfg["RequiredVariables"]
        cfg["RequiredVariables"] = content
    else:
      cfg["RequiredVariables"] = {}
    cfg = self.load_customizations(cfg)
    #cfg = self.fix_resource_separator_chars(cfg)
    last_config_loaded = cfg
    return cfg
  def fix_resource_separator_chars(self, config):
    if os.path.sep!='/':
      for k in config["Resources"]:
        k["url"]=k["url"].replace('/', os.sep)
    return config
                 
  @classmethod
  def new(cls, fileName):
    p = os.path.abspath(config.empty_template_path)
    if os.path.exists(p):
      shutil.copy(p, fileName)
      return cls(fileName)
    return None
