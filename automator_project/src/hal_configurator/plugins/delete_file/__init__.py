import os
from hal_configurator.lib.command_base import OperationBase, ArgumentDescriptor

class Operation(OperationBase):
  def __init__(self):
    pass
  def get_arg_descriptors(self):
    return [
            ArgumentDescriptor("FilePath", "The absolute file path of the file to be deleted", "text", os.path.exists)
            ]
  def run(self, **kwargs):
    os.remove(kwargs["FilePath"])
