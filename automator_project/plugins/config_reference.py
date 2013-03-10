from hal_configurator.lib.config_loaders import FileConfigLoader
__author__ = 'Costa Halicea'

from hal_configurator.lib.command_base import \
  OperationBase, InvalidCommandArgumentsError, ArgumentDescriptor

class ExecuteExternalConfig(OperationBase):
  """Replaces File(Destination) from a resource file supplied by URI"""

  def __init__(self,*args, **kwargs):
    super(ExecuteExternalConfig, self).__init__(*args, **kwargs)
    self.result = ''

  def set_args(self, ConfigPath):
    """
    :param ConfigPath:
    :type ConfigPath: str
    """
    self.kwargs["ConfigPath"] = self.ConfigPath = ConfigPath

  def run(self):
    is_valid, errors = self.validate_args()
    res = None
    if is_valid:
        res = self.value_substitutor.substitute(self.ConfigPath)
    else:
      raise InvalidCommandArgumentsError(str(errors))
    loader = FileConfigLoader(self.ConfigPath)
    config = loader.load_config()
    builder = self.executor.parent
    builder.apply_parametrized(config)

  @classmethod
  def get_arg_descriptors(cls):
    return [
      ArgumentDescriptor("ConfigPath", "External Configuration Directory", "text")
    ]

  @classmethod
  def get_name(cls):
    return "Run External Configuration"

__plugin__ = ExecuteExternalConfig