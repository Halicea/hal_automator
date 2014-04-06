'''
Created on Dec 22, 2013
@author: Costa Halicea
'''
class BaseProperty(object):
  def __getitem__(self, key):
    if isinstance( key, ( int, long ) ):
      return self.__dict__.keys()[key]
    if key in self.__dict__:
      return getattr(self, key)
    elif "is_"+key in self.__dict__:
      return getattr(self, "is_"+key)
    else: raise KeyError('Key %s is not part of this Object'%key)

  def has_key(self, key):
    return self.__contains__(key)

  def __setitem__(self, key, value):
    if key in self.__dict__:
      return setattr(self, key, value)
    elif "is_"+key in self.__dict__:
      return setattr(self, "is_"+key, value)
    else: raise KeyError('Key %s is not part of this Object'%key)

  def __contains__(self, key):
    return  key in self.__dict__ or "is_"+key in self.__dict__

  def iteritems(self):
    for k in self.__dict__.keys():
      if k.startswith('is_'):
        yield (k[3:], getattr(self, k))
      else:
        yield (k, getattr(self, k))


  def keys(self):
    for k in self.__dict__.keys():
      if k.startswith('is_'):
        yield k[3:]
      else:
        yield k
  def items(self):
    return self.iteritems()

  def __init__(self, display=None, helptext=None, validators=[]):
    self.display = display
    self.helptext = helptext
    self.validators = validators
    self.is_admin_only = False,
    self.is_required=True
    self.is_editable = False
    self.is_editable = True
    self.is_from_req = False

  @classmethod
  def from_dict(cls, d):
    result = cls()
    result.display =d['display'] if 'display' in d else ''
    result.helptext =d['helptext'] if 'helptext' in d else ''
    result.is_admin_only =d['admin_only'] if 'admin_only' in d else False
    result.is_required =d['required'] if 'required' in d else True
    result.is_editable = d['editable'] if 'editable' in d else True
    result.validators =d['validators'] if 'validators' in d else []
    result.group =  d['group'] if 'group' in d else ""
    result.type =  d['type'] if 'type' in d else ""
    result.is_from_req = d['is_from_req'] if 'is_from_req' in d else False
    return result

  @property
  def dictionary(self):
    return {
      "display":self.display,
      "helptext":self.helptext,
      "admin_only": self.is_admin_only,
      "required":self.is_required,
      "editable":self.is_editable,
      "validators":self.validators,
      "group":self.group,
      "type":self.type,
      "is_from_req": self.is_from_req
     }
  def set_dictionary(self, value):
    self.display =value['display'] if 'display' in value else self.display
    self.group =value['group'] if 'group' in value else self.group
    self.group =value['type'] if 'type' in value else self.type
    self.is_from_req =value['is_from_req'] if 'is_from_req' in value else self.is_from_req
    self.helptext =value['helptext'] if 'helptext' in value else self.helptext
    self.is_admin_only =value['admin_only'] if 'admin_only' in value else self.is_admin_only
    self.is_required =value['required'] if 'required' in value else self.is_required
    self.is_editable = value['editable'] if 'editable' in value else self.is_editable
    self.validators =value['validators'] if 'validators' in value else self.validators

class HalVar(BaseProperty):
  def __init__(self, value=None, name=None, display=None, helptext=None, validators = []):
    super(HalVar, self).__init__(display, helptext, validators)
    self.value = value
    self.name = name
    self.options = []

  @classmethod
  def from_dict(cls, d):
    res = super(HalVar, cls).from_dict(d)
    res.value =d['value'] if 'value' in d else ''
    res.name =d['name'] if 'name' in d else ''
    res.options = d['options'] if 'options' in d else None
    return res

  @property
  def dictionary(self):
    res = super(HalVar, self).dictionary
    res['value']=self.value
    res['name']=self.name
    if self.options:
      res['options'] = self.options
    return res

  @dictionary.setter
  def dictionary(self, value):
    super(HalVar, self).set_dictionary(value)
    self.name = value['name'] if 'name' in value else self.name
    self.value = value['value'] if 'value' in value else self.value

  def __repr__(self):
    return repr(self.__dict__)

  def __str__(self):
    return repr(self.__dict__)

class HalResource(BaseProperty):
  def __init__(self, rid=None, url=None, display=None, helptext=None, validators = []):
    super(HalResource, self).__init__(display, helptext, validators)
    self.rid = rid
    self.url = url

  @classmethod
  def from_dict(cls, d):
    res = super(HalResource, cls).from_dict(d)
    res.rid =d['rid'] if 'rid' in d else ''
    res.url =d['url'] if 'url' in d else ''
    return res

  @property
  def dictionary(self):
    res = super(HalResource, self).dictionary
    res["rid"]=self.rid
    res["url"]=self.url
    return res

  @dictionary.setter
  def dictionary(self, value):
    super(HalResource, self).set_dictionary(value)
    self.rid =value['rid'] if 'rid' in value else self.rid
    self.url =value['url'] if 'url' in value else self.url


