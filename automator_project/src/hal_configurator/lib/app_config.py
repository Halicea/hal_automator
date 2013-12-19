import os
from config import Config
import codecs
import json
try:
  from hal_configurator.lib.workspace_manager import Workspace
except:
  pass

__author__ = 'Costa Halicea'
__d = os.path.dirname(
        os.path.dirname(
          os.path.dirname(__file__)))

config_path = os.path.join(__d, 'config.conf')
config = Config(open(config_path, 'r'))


def add_config_to_history(path):
  ch = get_config_history()
  if path in ch:
    ch.append(ch.pop(ch.index(path)))
  elif len(config.config_history)==len(ch):
    ch.append("'"+path+"'")
    ch.pop(0)
  else:
    ch.append("'"+path+"'")
  for i in range(0, len(ch)):
    config.config_history[i].path=ch[i]
  save()

def get_config_history():
  return [k.path for k in config.config_history if k.path]

def get_current_workspace():
  if not Workspace.current:
    Workspace.set(config.current_workspace)
  return Workspace.current



def set_current_workspace(path):

  if not Workspace.current or Workspace.current.workspacedir!=path:  # @UndefinedVariable
    Workspace.set(path)
    config.current_workspace = "'%s'"%path
    save()

def get_working_dir():
  return config.working_dir_history[0].path

def set_working_dir(path):
  config.working_dir_history[0].path = "'"+path+"'"
  save()

def get_last_dir():
  return config.last_dir

def get_version():
  return config.version

def set_last_dir(d):
  config.last_dir = "'"+d+"'"
  save()

def save():
  s = open(config_path, 'w')
  config.save(s)
  s.close()