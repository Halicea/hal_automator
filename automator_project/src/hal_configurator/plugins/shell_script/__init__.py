from hal_configurator.lib.command_base import OperationBase, InvalidCommandArgumentsError,\
  ArgumentDescriptor
  
class ShellScript(OperationBase):

  def __init__(self, *args, **kwargs):
    super(ShellScript, self).__init__(*args, **kwargs)
    
  def get_result(self):
    return OperationBase.get_result(self)
  
  @classmethod
  def get_name(cls):
    return "Execute Shell Script"

  @classmethod
  def get_arg_descriptors(cls):
    return [
            ArgumentDescriptor("command", "shell command that will be executed", "text"),
            ArgumentDescriptor("is sudo", "Whether to execute with sudo privileges", "boolean"),
            ArgumentDescriptor("catch shell output", "Whether the result should be the shell output", "boolean")
           ]


  def run(self):
    return OperationBase.run(self)

  