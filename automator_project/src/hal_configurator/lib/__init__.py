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

  current =  os.path.abspath(__file__)
  current = os.path.dirname(os.path.dirname(current))
  res = os.path.join(current, 'config.conf')
  if not os.path.exists(res):
    if sys.platform =='darwin':
      print 'in Mac'
      res = os.path.join(os.getcwd(), 'config.conf')
      print res
      return res
  print res
  return res

