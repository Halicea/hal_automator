import os
import json
import traceback
import subprocess
base_settings = {
                 'branch':'master',
                 'user':'costa'
                }
class Workspace(object):
  current = None
  @staticmethod
  def set(workspacedir):
    Workspace.current = Workspace(workspacedir)

  def __init__(self, workspacedir):
    self.workspacedir = workspacedir
    self.settings_file = os.path.join(self.workspacedir, '.hal_workspace')
    self.settings = None
    self.__load_workspace_settings__()
    
  def __load_workspace_settings__(self):
    if os.path.exists(self.settings_file):
      self.settings = json.loads(open(self.settings_file).read())
    else:
      self.settings = base_settings
      self.save()
      
  def save(self):
    open(self.settings_file, 'w').write(json.dumps(self.settings))
    
  def _call(self, command, just_print=False):
    cmd = command
    if isinstance(command, (str, unicode)):
      cmd = command.split(' ')
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE,
                       close_fds=True, env=os.environ)
    output = []
    for line in iter(p.stdout.readline, b''):
      output.append(line[:-1])
      if just_print:
        print line
    return output
  
  def sync(self):
    old_cwd = os.getcwd()
    os.chdir(self.workspacedir)
    try:
      self._call('git add .'.split(' '))
      self._call('git commit -am "Commit"'%self.settings['user'])
      self._call('git pull origin master')
      self._call('git pull origin master')
    except:
      traceback.print_stack()
    finally:
      os.chdir(old_cwd)
    
    
  
  
  