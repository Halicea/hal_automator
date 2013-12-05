import sys
import traceback
from hal_configurator.lib.workspace_manager import Workspace


class DebugSettings(object):
  def __init__(self, set_breakpoint=True):
    self.breakpoint = set_breakpoint

class OperationBase(object):
  def __init__(self, executor, resources, variables, log=sys.stdout, verbose= False, *args, **kwargs):
    """
    :param args:
    :param kwargs:
    :param verbose: if True the output will be verbose
    :type verbose:bool
    :param executor: Executor of the command
    :type executor: CommandExecutor
    :param resources: resources available for the command
    :type resources:dict
    :param variables: variables available for the command
    :type variables: dict
    :param log: The Logger for the operation
    :type log: LoggerBase
    """
    self.kwargs = {}
    self.executor = executor
    self.resources = resources
    self.variables = variables
    self.value_substitutor = VarSubstitutor(self.variables, self.resources, self.executor.resources_root)
    self.log = log
    self.verbose = verbose
    self.description = ""
    self.result = ''

  def real_run(self):
    sign = "(%s)->%s"%(self.description, self.get_code())
    if self.verbose:
      self.log.write("START %s" % sign)
      for k in self.get_arg_descriptors():
        self.log.write("\tp: %s:%s" % (k.name, self.kwargs[k.name]))
    try:
      self.run()
    except:
      tb = traceback.format_exc()
      self.log.write("Error:%s"%repr(tb))
      raise
    finally:
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
    from hal_configurator.lib.plugin_loader import get_command_for_plugin
    return get_command_for_plugin(cls)

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

  @staticmethod
  def register_bundle(bundle_name):
    Workspace.registered_bundles.append(bundle_name)  # @UndefinedVariable

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
  "list": lambda x:True,
  "OperationBundle": lambda x:True
}

class ArgumentDescriptor(object):
  def __init__(self, name, description, argument_type, validator=None, is_optional=False, default_value_lambda=None):
    self.name = name
    self.argument_type = argument_type
    self.description = description
    if validator:
      self.validator = validator
    else:
      self.validator = self.default_validator
    self.is_optional = is_optional
    self.default_value_lambda = default_value_lambda

  def default_validator(self, value):
    if ArgumentTypes.has_key(self.argument_type):
      return ArgumentTypes[self.argument_type](value)
    return False, "Incompatible Type"

  def validate_argument(self, argument):
    return self.validator(argument)


from hal_configurator.lib.var_substitutor import VarSubstitutor
