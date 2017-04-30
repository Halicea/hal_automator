import traceback
import json
try:
  from hal_configurator.lib.workspace_manager import Workspace
except:
  pass
from hal_configurator.lib.dict2obj import DynamicObject
from hal_configurator.lib import config_path

__author__ = 'Costa Halicea'


class Config(DynamicObject):
  def __init__(self, d):
    j = json.loads(d)
    DynamicObject.__init__(self, j)

config = None
try:
  config = Config(open(config_path(), 'r').read())
except:
  traceback.print_exc()
  print(('ConfigPath %s' % config_path()))
  print('Cannot Locate the Configuration file')

def add_config_to_history(path):
  ch = get_config_history()
  if path in ch:
    ch.append(ch.pop(ch.index(path)))
  
  ch.append(path)
  if len(config.config_history) >= 10:
    ch.pop(0)
  save()

def get_config_history():
  return config.config_history

def get_current_workspace():
  if not Workspace.current:
    Workspace.set(config.current_workspace)
  return Workspace.current

def set_current_workspace(path):
  if not Workspace.current or Workspace.current.workspacedir != path:
    Workspace.set(path)
    config.current_workspace = path
    save()

def get_working_dir():
  return config.working_dir_history[-1]

def set_working_dir(path):
  config.working_dir_history[-1] = path
  save()

def get_last_dir():
  return config.last_dir

def get_version():
  return config.version

def set_last_dir(d):
  config.last_dir = d
  save()

def is_verbose():
  try:
    return config.verbose is True
  except:
    config.verbose = False
    save()
    return config.verbose

def set_verbose(value):
  config.verbose = value
  save()

def save():
  config.save(config_path())