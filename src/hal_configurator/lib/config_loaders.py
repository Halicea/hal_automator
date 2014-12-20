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
from hal_configurator.lib.models.hal_var import HalVar, HalResource
last_config_loaded = None

class ConfigLoader(object):
  available_references = ["Content", "RequiredVariables", "RequiredResources", "Builds"]

  def __init__(self, *args, **kwargs):
    self.custom_bundles = []
    self.custom_vars = []
    self.custom_resources = []
    self.resources_root_url = None
    self.last_config_loaded = None

  def __load_config_dict__(self):
    raise NotImplementedError("abstract class accessed")

  def __save_dictionary__(self, *args, **kwargs):
    raise NotImplementedError("abstract class accessed")

  def __pop_reference__(self, cfg, key, forced_reference_key=None):
    raise NotImplementedError("abstract class accessed")

  def __load_reference__(self, cfg, key, forced_reference_key=None):
    raise NotImplementedError("abstract class accessed")

  def load_config(self):
    cfg = self.__load_config_dict__()
    for ref in ConfigLoader.available_references:
      self.__load_reference__(cfg, ref)
    cfg = self.verify_required_vars(cfg)
    cfg = self.load_customizations(cfg)
    cfg = self.__objectify_vars__(cfg)
    self.last_config_loaded = cfg
    return cfg

  def extend_var(self, target, src, excluded_keys=[]):
    for k in src.keys():
      if not (k in excluded_keys):
        if k in target:
          if src[k] is not None and src[k] != target[k]:
            target[k] = src[k]
        else:
          target[k] = src[k]
    return target

  def __sanitize_vars_before_save__(self, d, clean_required_vars=True, update_global_vars=False, wipe_var_values=False):
    rvars = d['RequiredVariables']
    if update_global_vars:
      for v in d['Variables']:
        editable = True if not ('editable' in v) else v['editable']
        required = False if not ('required' in v) else v['required']
        found = [rv for rv in rvars if rv['name'] == v['name']]
        excluded_keys = ['is_from_req']
        if editable:
          excluded_keys.append('value')

        if found:
          self.extend_var(found[0], v, excluded_keys)
        elif required or not editable:
          rvars.append(self.extend_var({}, v, excluded_keys))

      to_del = []
      for rv in rvars:
        found = [v for v in d['Variables'] if v['name'] == rv['name'] and (v['required'] or v['editable'] is False or v['admin_only'])]
        if not found:
          to_del.append(rv)
      for k in to_del:
        rvars.remove(k)

    if clean_required_vars:
      to_remove = []
      for v in d['Variables']:
        found = [rv for rv in rvars if rv['name'] == v['name']]
        if found:
          if found[0].has_key('editable') and not found[0]['editable']:
            to_remove.append(v)

          elif 'value' in found[0]:
            if found[0]['value'] == v['value']:
              to_remove.append(v)
          else:
            pass
      for v in to_remove:
        d['Variables'].remove(v)

    if wipe_var_values:
      for v in d['Variables']:
        found = [rv for rv in rvars if rv['name'] == v['name']]
        if found:
          v['value'] = found[0]['value']
        else:
          v['value'] = None

  def __objectify_vars__(self, cfg):
    obj_vars = []
    obj_req_vars = []
    obj_res = []
    obj_req_res = []
    keys_vars = {'Variables': obj_vars, 'RequiredVariables': obj_req_vars}
    keys_res = {'Resources': obj_res, 'RequiredResources': obj_req_res}
    for key in keys_vars.keys():
      if key in cfg:
        for v in cfg[key]:
          keys_vars[key].append(HalVar.from_dict(v))
    for key in keys_res.keys():
      if key in cfg:
        for v in cfg[key]:
          keys_res[key].append(HalResource.from_dict(v))

    cfg['Variables'] = obj_vars
    cfg['RequiredVariables'] = obj_req_vars
    cfg['Resources'] = obj_res
    cfg['RequiredResources'] = obj_req_res
    return cfg

  def __dictify_vars__(self, cfg):
    obj_vars = []
    obj_req_vars = []
    obj_res = []
    obj_req_res = []
    keys = {'Variables': obj_vars, 'RequiredVariables': obj_req_vars, 'Resources': obj_res, 'RequiredResources': obj_req_res}
    for key in keys.keys():
      if key in cfg:
        for v in cfg[key]:
          if isinstance(v, (HalVar, HalResource)):
            keys[key].append(v.dictionary)
          else:
            keys[key].append(v)
    cfg['Variables'] = obj_vars
    cfg['RequiredVariables'] = obj_req_vars
    cfg['Resources'] = obj_res
    cfg['RequiredResources'] = obj_req_res
    return cfg

  @property
  def dictionary(self):
    if not self.last_config_loaded:
      self.load_config()
    return self.__dictify_vars__(self.last_config_loaded)

  def save_config(self, cfg, save_references=False, is_new_config=False):
    self.__sanitize_vars_before_save__(cfg, clean_required_vars=True, update_global_vars=save_references, wipe_var_values=is_new_config)
    self.__dictify_vars__(cfg)
    for ref in FileConfigLoader.available_references:
      content, ref_path = self.__pop_reference__(cfg, ref)
      if save_references and content and ref_path:
        self.__save_dictionary__(content, ref_path)
    self.__save_dictionary__(cfg, self.resolved_path)

  def load_custom_bundles(self, config):
    config["Content"]["OperationBundles"].extend(self.custom_bundles)
    return config

  def load_custom_vars(self, config):
    variables = config["Variables"]
    existing_ones = [x for x in variables if len([y for y in self.custom_vars if y["name"] == x["name"]]) > 0]
    for k in existing_ones:
      variables.remove(k)
    variables.extend(self.custom_vars)
    return config

  def load_custom_resources(self, config):
    variables = config["Resources"]
    existing_ones = [x for x in variables if len([y for y in self.custom_vars if y["rid"] == x["rid"]]) > 0]
    for k in existing_ones:
      variables.remove(k)
    variables.extend(self.custom_resources)
    return config

  def validate(self):
    """validates the last loaded configuration"""
    raise NotImplementedError('this feature is not yet implemented')

  def verify_required_vars(self, config):
    variables = config["Variables"]
    required = config["RequiredVariables"]
    for rv in required:
      v = [x for x in variables if x["name"] == rv["name"]]
      if not v:
        variables.insert(0, copy.deepcopy(rv))
      else:
        if len(v) == 1:
          v = v[0]
        else:
          raise Exception('Variable %s is defined % times, it should be only once.' % (rv['name'], len(v)))
        for key in rv:
          if key != 'name' and key != 'value':
            if rv[key] is not None and rv[key] != '':
              v[key] = copy.deepcopy(rv[key])
        if rv.has_key('editable') and not rv['editable']:
          v['value'] = copy.deepcopy(rv['value'])
        v['is_from_req'] = True
    return config

  def append_bundles(self, *bundles):
    self.custom_bundles.extend(bundles)

  def append_vars(self, *custom_vars):
    self.custom_vars.extend(custom_vars)

  def load_customizations(self, cfg):
    cfg = self.load_custom_bundles(cfg)
    cfg = self.load_custom_vars(cfg)
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

  def __init__(self, fileName):
    super(FileConfigLoader, self).__init__()
    self._config_file_raw = fileName
    self.resolved_path = self.config_file = os.path.abspath(os.path.expanduser(self._config_file_raw))
    self.resources_root = os.path.abspath(os.path.dirname(self.resolved_path))
    self.resource_root_url = urllib.pathname2url(self.resources_root)

  def __load_config_dict__(self):
    global last_config_loaded
    cfg = json.load(open(self.resolved_path, 'r'))
    return cfg

  def __load_reference__(self, cfg, key, forced_reference_key=None):
    if cfg.has_key(key):
      if isinstance(cfg[key], dict) and cfg[key].has_key("Reference"):
        content_path = os.path.join(os.path.dirname(self.resolved_path), cfg[key]["Reference"])
        content = json.load(open(content_path, "r"))
        if forced_reference_key:
          cfg[forced_reference_key] = cfg[key]["Reference"]
        else:
          cfg[key+"-Reference"] = cfg[key]["Reference"]
        cfg[key] = content
    else:
      cfg[key] = {}

  def __save_dictionary__(self, content, filepath):
    f = open(filepath, 'w')
    f.write(json.dumps(content, sort_keys=True, indent=2))
    f.close()

  def __pop_reference__(self, cfg, key, forced_reference_key=None):
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
      cfg[key] = {"Reference": ref_path}
      return content, os.path.join(os.path.dirname(self.resolved_path), ref_path)
    else:
      return None, None

  def fix_resource_separator_chars(self, config):
    if os.path.sep != '/':
      for k in config["Resources"]:
        k["url"] = k["url"].replace('/', os.sep)
    return config

  @classmethod
  def new(cls, fileName):
    p = os.path.abspath(config.empty_template_path)
    if os.path.exists(p):
      shutil.copy(p, fileName)
      return cls(fileName)
    return None
