'''
Created on Jan 27, 2013
@author: Costa Halicea
'''
from inspect import isfunction
import json
class DynamicObject(object):
  '''The recursive class for building and representing objects with.'''
  def __init__(self, obj):
    for k, v in list(obj.items()):
      if isinstance(v, dict):
        setattr(self, k, DynamicObject(v))
      else:
        setattr(self, k, v)
        
  def __getitem__(self, val):
    return self.__dict__[val]
  
  def __setitem__(self, name, item):
    if isinstance (item, dict):
      item = DynamicObject(item)
    self.__dict__[name] = item
  
  def __repr__(self):
    return '{%s}' % str(', '.join('%s : %s' % (k, repr(v)) for
      (k, v) in self.props()))
      
  def props(self):
    for k, v in list(self.__dict__.items()):
      if not isfunction(v):
        yield k, v
  
  def save(self, path):
    import json
    with open(path, 'w') as fp:
        json.dump(self.to_dict(), fp, sort_keys=True, indent=4, separators=(',', ': '))
  
  def to_dict(self):
    d = {}
    for k, v in self.props():
      if isinstance(v, DynamicObject):
        d[k] = v.to_dict()
      elif isinstance(v, list):
        l = []
        for item in v:
          if isinstance(item, DynamicObject):
            l.append(item.to_dict())
          else:
            l.append(item)
        d[k] = l
      else:
        d[k] = v
    return d