import os
import re
import sys
from hal_configurator.lib.command_base import OperationBase

__author__ = 'Costa Halicea'


def get_plugins(plugin_dir):
  """Adds plugins to sys.path and returns them as a list
  :rtype : list
  """
  registered_plugins = []
  #check to see if a plugins directory exists and add any found plugins
  # (even if they're zipped)
  if os.path.exists(plugin_dir):
    plugins = [x for x in os.listdir(plugin_dir) \
               if not x.startswith('.') and\
               (x.endswith('.py') or os.path.isdir(os.path.join(plugin_dir, x)))]
    pattern = ".py$"
    for plugin in plugins:
      plugin_path = os.path.join(plugin_dir, plugin)
#      if os.path.splitext(plugin)[1] == ".zip":
#        sys.path.append(plugin_path)
#        (plugin, ext) = os.path.splitext(plugin) # Get rid of the .zip extension
#        registered_plugins.append(plugin)
      if plugin != "__init__.py":
        if re.search(pattern, plugin):
          (shortname, ext) = os.path.splitext(plugin) #@UnusedVariable
          registered_plugins.append(shortname)
      if os.path.isdir(plugin_path):
        plugins = os.listdir(plugin_path)
        for plugin in plugins:
          if plugin != "__init__.py":
            (shortname, ext) = os.path.splitext(plugin) #@UnusedVariable
            sys.path.append(plugin_path)
            registered_plugins.append(shortname)
  return registered_plugins

def init_plugin_system(cfg):
  """
  Initializes the plugin system by appending all plugins into sys.path and
  then using load_plugins() to import them.

      cfg - A dictionary with two keys:
      plugin_path - path to the plugin directory (e.g. 'plugins')
      plugins - List of plugin names to import (e.g. ['foo', 'bar'])
  """
  if not cfg['plugin_path'] in sys.path:
    sys.path.insert(0, cfg['plugin_path'])
  load_plugins(cfg['plugins'])

def load_plugins(plugins):
  """
  Imports all plugins given a list.
  :param plugins:
  Note:  Assumes they're all in sys.path.
  """
  for plugin in plugins:
    __import__(plugin, None, None, [''])
    if plugin not in OperationBase.__subclasses__(): #@UndefinedVariable
      # This takes care of importing zipped plugins:
      __import__(plugin, None, None, [plugin])
__plugins_list__ = []
def load_plugins_from_directory_list(plugin_dirs):
  """
  Loads all the plugins found in a specific directory
  :param plugin_dirs:
  :type plugin_dirs: list
  """
  for plugin_dir in plugin_dirs:
    plugin_list = get_plugins(plugin_dir)
    init_plugin_system({'plugin_path': plugin_dir, 'plugins': plugin_list})
    for p in plugin_list:
      module=get_plugin_module(p)
      if hasattr(module, '__plugins__'):
        for plugClass in module.__plugins__:
          __plugins_list__.append('%s.%s'%(p, plugClass.__name__))
      if hasattr(module,'__plugin__'):
        __plugins_list__.append(p)

def get_plugins_list():
  return list(set(__plugins_list__))

def get_plugin_cls(command):
  cmd  = isinstance(command, (str, unicode)) and command or command["Code"]
  module, claz = get_module_and_class_names_from_cmd(cmd)
  plugin_module = __import__(module)
  plugin_cls = None
  if claz:
    plugin_cls = eval('plugin_module.%s'%claz)
  else:
    plugin_cls = plugin_module.__plugin__
  return plugin_cls


def get_plugin_module(command):
  cmd  = isinstance(command, str) and  command or command["Code"]
  module, claz =  get_module_and_class_names_from_cmd(cmd) #@UnusedVariable
  return __import__(module)

def get_module_and_class_names_from_cmd(cmd):
  if '.' in cmd:
    a = cmd.split('.')
    return a[0], a[1]
  else:
    return cmd, None

def get_command_for_plugin(plugin_cls):
  module = plugin_cls.__module__
  cls_name = plugin_cls.__name__
  matched = filter(lambda x:x.startswith(module), get_plugins_list())
  if len(matched)==1:
    return matched[0]
  elif len(matched)>1:
    final = filter(lambda x:x.endswith(cls_name), matched)
    if len(final)>0:
      return final[0]
  return None
