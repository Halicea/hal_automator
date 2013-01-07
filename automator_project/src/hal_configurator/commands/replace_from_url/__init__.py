
from lib.command_base import CommandBase, InvalidCommandArgumentsError
import re
import glob

class ReplaceFromUrl(CommandBase):
  """Replaces File(Destination) from a resource file supplied by URI"""
  def __init__(self, Resource, Destination):
    self.Resource = Resource
    self.Destination = Destination
    errors = self.__validate_input__()
    if errors:
      raise InvalidCommandArgumentsError(' AND '.join(errors))

  def __validate_input__(self):
    error_messages =[]
    if not(self.Resource and self.Destination):
      return ["One or more parameters are not supplied"]
    return error_messages
  
  def run(self):
    pass
  
      