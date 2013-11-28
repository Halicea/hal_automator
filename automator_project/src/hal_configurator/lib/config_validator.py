'''
Created on Nov 28, 2013

@author: kostamihajlov
'''
import os
MSG_REQUIRED_BUT_EMPTY = "Variable %s is requires a value but instead it's empty"
MSG_REQUIRED_BUT_NOT_FOUND = "Variable %s is required"
MSG_WORKING_DIR_NOT_EXISTS = "The chosen working directory \"%s\" does not cannot be found on the file system"
MSG_WORKING_DIR_IS_FILE = "The chosen working directory \"%s\" is a file, it should be a valid folder"
 
class ConfigurationValidator(object):
  
  '''
  Validates if the required variables and all the resources are present in the configuration
  Validates if the working directory exists
  Uses custom validators in the variables to validate the validity of their input 
  '''
  def __init__(self):
    self.is_valid = None
    
  def v_required_vars(self, configurator):
    config = configurator.config
    messages = []
    reqvars = config['RequiredVariables']
    actual_vars = config['Variables']
    for rv in reqvars:
      found = False
      for v in actual_vars:
        if v['name'] == rv['name']:
          found = True
          if rv['required'] and not v['value'] and not rv['value']:
            messages.append(MSG_REQUIRED_BUT_EMPTY % v['name'])
        if found: break
      if not found:
        messages.append(MSG_REQUIRED_BUT_NOT_FOUND % rv['name'])

  def v_resources(self, configurator):
    return True
  
  def v_working_dir(self, configurator):
    messages = []
    if os.path.exists(configurator.working_dir):
      if os.path.isdir(configurator.working_dir):
        return messages
      else:
        messages.append(MSG_WORKING_DIR_IS_FILE % configurator.working_dir)
    else:
      messages.append(MSG_WORKING_DIR_NOT_EXISTS % configurator.working_dir)
   
    
  def validate(self, config):
    messages = self.v_required_vars(config)
    messages.extend(self.v_resources(config))
    self.is_valid = len(messages) == 0
    return messages
  
