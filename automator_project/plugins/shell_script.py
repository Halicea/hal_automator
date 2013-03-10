import os
import subprocess
import time
from hal_configurator.lib.command_base import OperationBase, InvalidCommandArgumentsError,\
  ArgumentDescriptor
from subprocess import call
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
            ArgumentDescriptor("working directory", "relative or absolute path where the command will be executed", "text"),
            ArgumentDescriptor("command", "shell command that will be executed", "text"),
            ArgumentDescriptor("is sudo", "Whether to execute with sudo privileges", "boolean"),
            ArgumentDescriptor("catch shell output", "Whether the result should be the shell output", "boolean")
           ]

  def set_args(self, **kwargs):
    self.kwargs = kwargs
    is_valid, errors = self.validate_args()
    if is_valid:
      self.command = self.kwargs["command"]
      self.is_sudo = self.kwargs["is sudo"]
      self.catch_shell_output = bool(kwargs["catch shell output"])
      self.working_dir = self.kwargs["working directory"].startswith("/") and self.kwargs["working directory"] or \
                         os.path.join(os.getcwd(), self.kwargs["working directory"])
    else:
      raise InvalidCommandArgumentsError(str(errors))

  def run(self):
    print os.getcwd()
    cmd = self.command.split(' ')

    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE,
                         close_fds=True, cwd=self.working_dir, env=os.environ)

    stdout = p.stdout
    while(True):
      p.poll() #returns None while subprocess is running
      line = stdout.readline()
      #time.sleep(0.1)
      self.log.write("  >>>%s"%line[:-1])
      if (line == "" and p.returncode != None):
        break
    stdout.close()
__plugin__ = ShellScript