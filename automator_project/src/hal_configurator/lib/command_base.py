import sys
from hal_configurator.lib.var_substitutor import VarSubstitutor

class DebugSettings(object):
  def __init__(self, set_breakpoint=True):
    self.breakpoint = set_breakpoint
    
class OperationBase(object):
  code = "shell_script"
  def __init__(self, *args, **kwargs):
    self.kwargs = {}
    if kwargs.has_key('verbose'):
      self.verbose = kwargs['verbose']
    else:
      self.verbose = False
    self.executor = kwargs["executor"]
    self.resources = kwargs['resources']
    self.variables = kwargs['variables']
    self.value_substitutor = VarSubstitutor(self.variables, self.resources, self.executor.resources_root)
    self.log = kwargs.has_key("log") and kwargs["log"] or sys.stdout
    self.description = ""
    self.result = ''
    
  def real_run(self):
    sign = "(%s)->%s"%(self.description, self.code)
    if self.verbose:
      self.log.write("START %s" % sign)
      for k in self.get_arg_descriptors():
        self.log.write("\tp: %s:%s" % (k.name, self.kwargs[k.name]))
    self.run()
    if self.verbose: self.log.write("END %s"%sign)


  def get_result(self):
    return self.result
  
  def set_args(self, **kwargs):
    self.kwargs = kwargs
  
  def get_dict(self):
    return {
            "Code":self.get_code(),
            "Type":self.get_name(), 
            "Arguments":dict([(x.name, self.kwargs.has_key(x.name) and self.kwargs[x.name] or "") for x in self.get_arg_descriptors()])
           }
  @classmethod
  def get_empty_dict(cls):
    return{
            "Code":cls.get_code(),
            "Type":cls.get_name(), 
            "Arguments":dict([(x.name, "") for x in cls.get_arg_descriptors()])
           }
  @classmethod
  def get_name(cls):
    return cls.__name__
  
  @classmethod
  def get_code(cls):
    return cls.code
  
  @classmethod
  def get_arg_descriptors(cls):
    raise NotImplementedError("Method get_arg_descriptors is not implemented")
  
  def validate_args(self):
    errors = []
    descriptors = self.get_arg_descriptors()
    for k in descriptors:
      if self.kwargs.has_key(k.name):
        v = k.validate_argument(self.kwargs[k.name])
        if not v:
          errors.append(v)
    if errors:
      return False, errors
    else:
      return True, errors
  
  def run(self):
    raise NotImplementedError("Method get_arg_descriptors is not implemented")
  
class InvalidCommandArgumentsError(Exception):
  def __init__(self, message=None):
    super(InvalidCommandArgumentsError, self).__init__(message)

def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    return False
      
ArgumentTypes = {
  "text": lambda x: True, 
  "number": lambda x: is_number(x), 
  "date": lambda x: True,
  "file": lambda x: True,
  "list": lambda x:True
}

class ArgumentDescriptor(object):
  def __init__(self, name, description, argument_type, validator=None):
    self.name = name
    self.argument_type = argument_type
    self.description = description
    if validator:
      self.validator = validator
    else:
      self.validator = self.default_validator
  
  def default_validator(self, value):
    if ArgumentTypes.has_key(self.argument_type):
      return ArgumentTypes[self.argument_type](value)
    return False, "Incompatible Type"
  
  def validate_argument(self, argument):
    return self.validator(argument)
