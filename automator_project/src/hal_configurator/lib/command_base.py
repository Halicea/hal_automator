
class OperationBase(object):
  def __init__(self, *args, **kwargs):
    self.kwargs = {}
    if kwargs.has_key('verbose'):
      self.verbose = kwargs['verbose']
    else:
      self.verbose = False
    self.result = ''
  
  def get_result(self):
    return self.result
  
  def set_args(self, **kwargs):
    self.kwargs = kwargs
  
  @classmethod
  def get_name(cls):
    return cls.__name__
  
  def get_arg_descriptors(self):
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
    
      
    
  
