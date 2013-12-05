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
import copy
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
        variables.insert(0, copy.deepcopy(rv))
      else:
        if len(v)==1:
          v = v[0]
        else:
          raise Exception('Variable %s is defined % times, it should be only once.'%(rv['name'], len(v)))
        for key in rv:
          if key!='name' and key!='value':
            if rv[key]!=None and rv[key]!='':
              v[key] = copy.deepcopy(rv[key])
        if rv.has_key('editable') and not rv['editable']:
          v['value'] = copy.deepcopy(rv['value'])
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
  available_references = ["Content", "RequiredVariables", "Builds"]
  def __init__(self, fileName):
    super(FileConfigLoader, self).__init__()
    self.config_file = fileName
    self.resources_root = os.path.abspath(os.path.dirname(self.config_file))
    self.resource_root_url = urllib.pathname2url(self.resources_root)

  def load_config(self):
    global last_config_loaded
    print os.path.abspath(self.config_file)
    cfg =  json.load(open(self.config_file, 'r'))
    for ref in FileConfigLoader.available_references:
      try:
        self.__load_reference__(cfg, ref)
      except Exception, ex:
        print ex.message
        print "Cannot load reference", ref
        raise ex
    cfg = self.load_customizations(cfg)
    last_config_loaded = cfg
    return cfg

  def __load_reference__(self, cfg, key, forced_reference_key = None):
    if cfg.has_key(key):
      if cfg[key].has_key("Reference"):
        content_path = os.path.join(os.path.dirname(self.config_file), cfg[key]["Reference"])
        content = json.load(open(content_path , "r"))
        if forced_reference_key:
          cfg[forced_reference_key] =  cfg[key]["Reference"]
        else:
          cfg[key+"-Reference"] = cfg[key]["Reference"]
        cfg[key] = content
    else:
      cfg[key] = {}

  def save_config(self, cfg, save_references=False):
    for ref in FileConfigLoader.available_references:
      content, ref_path = self.__pop_reference__(cfg, ref)
      if save_references and content and ref_path:
        self.__save_dictionary__(content, ref_path)
    self.__save_dictionary__(cfg, self.config_file)

  def __save_dictionary__(self, content, filepath):
    f = open(filepath, 'w')
    f.write(json.dumps(content, sort_keys = True, indent = 2))
    f.close()



  def __pop_reference__(self, cfg, key, forced_reference_key = None):
    ref_path = None
    content = {}
    if forced_reference_key:
      if cfg.has_key(forced_reference_key):
        ref_path = cfg[forced_reference_key]
        del cfg[forced_reference_key]
    else:
      if cfg.has_key(key+"-Reference"):
        ref_path = cfg[key+"-Reference"]
        del cfg[key+"-Reference"]
    if ref_path:
      content = cfg[key]
      cfg[key]={"Reference":ref_path}
      return content, os.path.join(os.path.dirname(self.config_file), ref_path)
    else:
      return None, None



  #TODO: Implement a save method for the config

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
