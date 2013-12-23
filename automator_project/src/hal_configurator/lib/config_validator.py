import os
import re
MSG_REQUIRED_BUT_EMPTY = "Variable %s should not be empty"
MSG_REQUIRED_BUT_NOT_FOUND = "Variable %s is required"
MSG_REQUIRED_BUT_EMPTY_RES = "Resource %s is not set"
MSG_WORKING_DIR_NOT_EXISTS = "The chosen working directory \"%s\" does not cannot be found on the file system"
MSG_WORKING_DIR_IS_FILE = "The chosen working directory \"%s\" is a file, it should be a valid folder"
MSG_UNUSED_VAR = 'Variable %s is defined but it\'s value is never used'
MSG_UNUSED_RES = 'Resource %s is defined but it\'s value is never used'
MSG_SUGGEST_VAR_PROPERTY = "Variable %s should have '%s' property defined"
MSG_UNDECLARED_VAR = "Variable %s is used but it is not declared"
MSG_UNDECLARED_RES = "Resource %s is used but it is not declared"

class ValidationResult(object):
  def __init__(self):
    self.warnings =[]
    self.errors = []
    self.suggestions = []
    self.is_valid = True

  def extend(self, result):
    self.warnings.extend(result.warnings)
    self.errors.extend(result.errors)
    self.suggestions.extend(result.suggestions)
    self.is_valid =self.is_valid and result.is_valid
    return self

  def __repr__(self):
    message = 'Errors:\n'+'\n'.join(['\tError: '+x for x in self.errors])
    message+= '\nWarnings:\n'+'\n'.join(['\tWarn: '+x for x in self.warnings])
    message+= '\nSuggestions:\n'+'\n'.join(['\tSuggestion: '+x for x in self.suggestions])
    return message

  def __str__(self):
    return self.__repr__()

class ConfigurationValidator(object):

  '''
  Validates if the required variables and all the resources are present in the configuration
  Validates if the working directory exists
  Uses custom validators in the variables to validate the validity of their input
  '''
  def __init__(self, config_path):
    self.config_path = config_path
    self.config_root = os.path.dirname(self.config_path)

  def v_required_vars(self, config):
    result = ValidationResult()
    reqvars = config['RequiredVariables']
    actual_vars = config['Variables']
    for rv in reqvars:
      found = False
      for v in actual_vars:
        if v['name'] == rv['name']:
          found = True
          if rv['required'] and not v['value'] and not rv['value']:
            result.is_valid = False
            result.errors.append(MSG_REQUIRED_BUT_EMPTY % v['name'])
        if found: break
      if not found:
        result.is_valid = False
        result.errors.append(MSG_REQUIRED_BUT_NOT_FOUND % rv['name'])
    return result

  def get_unused_vars(self, config):
    result = []
    s = str(config["Content"])
    for v in config["Variables"]:
      if not "{{"+v['name']+"}}" in s:
        result.append(v)
    return result

  def get_unused_resources(self, config):
    result = []
    s = str(config["Content"])
    for v in config["Resources"]:
      if not "{#"+v['rid']+"#}" in s:
        result.append(v)
    return result

  def get_suggestions(self, config):
    result = ValidationResult()
    var_suggested_keys=["display", "name", "type", "value", "admin_only", "required"]
    for v in config["Variables"]:
      for k in var_suggested_keys:
        if not k in v:
          result.suggestions.append(MSG_SUGGEST_VAR_PROPERTY%(v['name'], k))
    for v in config["RequiredVariables"]:
      for k in var_suggested_keys:
        if not k in v:
          result.suggestions.append(MSG_SUGGEST_VAR_PROPERTY%('(in required)'+v['name'], k))
    return result

  def get_undefined_vars(self, config):
    reserved_vars = ['item', 'index']
    result = ValidationResult()
    undeclared_vars = []
    s = str(config["Content"])
    search_pattern ="\{\{\w+\}\}"
    used_vars = [k[2:-2] for k in re.findall(search_pattern, s)]
    for v in list(set(used_vars)):
      if not v in reserved_vars:
        found = False
        for k in config["Variables"]:
          if k['name']==v:
            found=True
        if not found:
          undeclared_vars.append(v)

    for k in undeclared_vars:
      result.is_valid = False
      result.errors.append(MSG_UNDECLARED_VAR%k)
    return result

  def get_undefined_resources(self, config):
    result = ValidationResult()
    undeclared_resources = []
    s = str(config["Content"])
    search_pattern ="\{#\w+#\}"
    used_resources = [k[2:-2] for k in re.findall(search_pattern, s)]
    for v in list(set(used_resources)):
      found = False
      for k in config["Resources"]:
        if k['rid']==v:
          found=True
      if not found:
        undeclared_resources.append(v)

    for k in undeclared_resources:
      result.is_valid = False
      result.errors.append(MSG_UNDECLARED_RES%k)
    return result

  def get_unused_warnings(self, config):
    result = ValidationResult()
    v = self.get_unused_vars(config)
    r = self.get_unused_resources(config)
    for i in v:
      result.warnings.append(MSG_UNUSED_VAR%i['name'])
    for i in r:
      result.warnings.append(MSG_UNUSED_RES%i['rid'])
    return result

  def v_resources(self, config):
    result = ValidationResult()
    resources = config['Resources']
    for res in resources:
      if res['url']:
        absres = os.path.abspath(os.path.join(self.config_root, res['url']))
        if not os.path.exists(absres):
          result.is_valid = False
          result.errors.append(MSG_REQUIRED_BUT_EMPTY_RES%res['rid'])
      else:
        result.errors.append(MSG_REQUIRED_BUT_EMPTY_RES%res['rid'])
    return result

  def validate_working_dir(self, working_dir):
    result = ValidationResult()
    if os.path.exists(working_dir):
      if not os.path.isdir(working_dir):
        result.is_valid = False
        result.errors.append(MSG_WORKING_DIR_IS_FILE % working_dir)
    else:
      result.is_valid = False
      result.errors.append(os.path.abspath(os.getcwd()))
      result.errors.append(MSG_WORKING_DIR_NOT_EXISTS % working_dir)
    return result

  def validate(self, config, working_dir=None):
    result = self.v_required_vars(config)\
      .extend(self.v_resources(config))\
      .extend(self.get_unused_warnings(config))\
      .extend(self.get_suggestions(config))\
      .extend(self.get_undefined_vars(config))\
      .extend(self.get_undefined_resources(config))
    if working_dir:
      result.extend(self.validate_working_dir(working_dir))
    return result

