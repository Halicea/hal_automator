'''
Created on Dec 23, 2012

@author: kostamihajlov
'''
class GlobalVars(object):
  _instance = None
  @classmethod
  def get_instance(cls):
    if not cls._instance:
      cls._instance = GlobalVars()
    return cls._instance

  def __init__(self):
    self.current_config_path = None
  