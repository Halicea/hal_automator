import os
import shutil
import sys


def copytree(src, dst, symlinks=False, ignore=None):
  for item in os.listdir(src):
      s = os.path.join(src, item)
      d = os.path.join(dst, item)
      if os.path.isdir(s):
          shutil.copytree(s, d, symlinks, ignore)
      else:
          shutil.copy2(s, d)


def config_path():
  current = os.path.abspath(__file__)
  d = os.path.dirname
  current = d(d(d(current)))
  res = os.path.join(current, 'config.conf')
  res = os.path.expanduser(res)
  print 'Trying:', res
  if not os.path.exists(res):
    print('Error: path {} does not exists'.format(res))
    if sys.platform == 'darwin':
      print 'in Mac'
      res = os.path.join(os.getcwd(), 'config.conf')
      print res
      return res
  print res
  return res


def load_plugins():
  from .app_config import config
  from .plugin_loader import load_plugins_from_directory_list
  if config:
      plugin_dirs = []
      cp = config_path()
      j = os.path.join
      dn = os.path.dirname
      abp = os.path.abspath
      for p_dir in config.plugin_dirs:
          if os.path.isabs(p_dir):
              plugin_dirs.append(p_dir)
          else:
              abs_dir = abp(j(dn(cp), p_dir))
              plugin_dirs.append(abs_dir)
      load_plugins_from_directory_list(plugin_dirs)
  else:
      print 'No Configuration Loadeed, Continuing...'

  sys.path.append(os.path.abspath(__file__))
