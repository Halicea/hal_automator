'''
Created on Dec 22, 2013
@author: Costa Halicea
'''

class HalVar(object):
  def __init__(self, value=None, name=None, display=None, helptext=None, validators = []):
    self.value = value
    self.name = name
    self.display = display
    self.helptext = helptext
    self.admin_only = False,
    self.required=True
    self.validators = validators

  @property
  def dictionary(self):
    return {
            "value":self.value,
            "name":self.name,
            "display":self.display,
            "helptext":self.helptext,
            "admin_only": self.admin_only,
            "validators":self.validators,
            "required":self.required
    }
  @dictionary.setter
  def dict(self, value):
    for k in value.keys():
      if k in self.__dict__:
        setattr(self, k, value[k])

class HalResource(object):
  def __init__(self, rid=None, url=None, display=None, helptext=None, validators = []):
    self.rid = rid
    self.url = url
    self.display = display
    self.helptext = helptext
    self.admin_only = False,
    self.required=True
    self.validators = validators

  @property
  def dictionary(self):
    return {
            "rid":self.rid,
            "url":self.url,
            "display":self.display,
            "helptext":self.helptext,
            "admin_only": self.admin_only,
            "validators":self.validators,
            "required":self.required
    }
  @dictionary.setter
  def dict(self, value):
    for k in value.keys():
      if k in self.__dict__:
        setattr(self, k, value[k])







