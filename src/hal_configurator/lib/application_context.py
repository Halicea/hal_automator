'''
Created on Nov 28, 2013

@author: kostamihajlov
'''
class UIModes(object):
  Admin = 'admin'
  Moderator = 'moderator'
  Publisher = 'publisher'

class ApplicationContext(object):
  __instance__  = None
  @staticmethod
  def get_instance():
    if not ApplicationContext:
      __instance__ = ApplicationContext()
    return __instance__
    
  def __init__(self):
    self.user = None
    self.ui_mode = 'admin'
    
    