class CommandBase(object):
  def __init__(self, *args, **kwargs):
    pass
  def run(self,*args, **kwargs):
    raise NotImplementedError("Method run is not implemented")

class InvalidCommandArgumentsError(Exception):
  def __init__(self, message=None):
    super(InvalidCommandArgumentsError, self).__init__(message)
