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
    plugins = os.listdir(plugin_dir)
    pattern = ".py$"
    for plugin in plugins:
      plugin_path = os.path.join(plugin_dir, plugin)
      if os.path.splitext(plugin)[1] == ".zip":
        sys.path.append(plugin_path)
        (plugin, ext) = os.path.splitext(plugin) # Get rid of the .zip extension
        registered_plugins.append(plugin)
      elif plugin != "__init__.py":
        if re.search(pattern, plugin):
          (shortname, ext) = os.path.splitext(plugin)
          registered_plugins.append(shortname)
      if os.path.isdir(plugin_path):
        plugins = os.listdir(plugin_path)
        for plugin in plugins:
          if plugin != "__init__.py":
            if re.search(pattern, plugin):
              (shortname, ext) = os.path.splitext(plugin)
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
    if plugin not in OperationBase.__subclasses__():
      # This takes care of importing zipped plugins:
      __import__(plugin, None, None, [plugin])

def load_plugins_from_directory_list(plugin_dirs):
  """
  Loads all the plugins found in a specific directory
  :param plugin_dirs:
  :type plugin_dirs: list
  """
  for plugin_dir in plugin_dirs:
    plugin_list = get_plugins(plugin_dir)
    init_plugin_system({'plugin_path': plugin_dir, 'plugins': plugin_list})

def get_plugin_cls(command):
  cmd  = command["Code"]
  plugin_module = __import__(cmd)
  plugin_cls = plugin_module.__plugin__
  return plugin_cls