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
    if os.path.exists(workspacedir):
      Workspace.current = Workspace(workspacedir)
    else:
      Workspace.current = None

  def __init__(self, workspacedir):
    self.workspacedir = workspacedir
    self.settings_file = os.path.join(self.workspacedir, '.hal_workspace')
    self.settings = None
    self.loger = None

    self.__load_workspace_settings__()

  def set_loger(self, loger):
    self.loger = loger
  @property
  def mode(self):
    return self.settings.has_key('mode') and self.settings['mode'] or 'admin'

  def __load_workspace_settings__(self):
    if os.path.exists(self.settings_file):
      self.settings = json.loads(open(self.settings_file).read())
    else:
      self.settings = base_settings
      self.save()

  def save(self):
    open(self.settings_file, 'w').write(json.dumps(self.settings))

  def _call(self, command, just_print=True):
    cmd = command
    if isinstance(command, (str, unicode)):
      cmd = command.split(' ')
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE,
                       close_fds=True, env=os.environ)
    output = []
    for line in iter(p.stdout.readline, b''):
      output.append(line[:-1])
      if just_print:
        if self.loger:
          self.loger.write(line)
        print line
    return output

  def sync(self):
    old_cwd = os.getcwd()
    os.chdir(self.workspacedir)
    try:
      self._call('git add .')
      self._call(["git", "commit", '-am Commit by %s'%self.settings['user']])
      self._call('git pull origin %s'%self.settings['branch'])
      self._call('git push origin %s'%self.settings['branch'])
      self.loger.write('\n FINISHED \n')
    except:
      traceback.print_exc()

    finally:
      os.chdir(old_cwd)
  def reset(self):
    old_cwd = os.getcwd()
    os.chdir(self.workspacedir)
    try:
      self._call('git fetch origin')
      self._call('git reset --hard origin/%s'%self.settings['branch'])
      self.loger.write('\n FINISHED \n')
    except:
      ss = traceback.format_exc()
      if self.loger:
        self.loger.write(traceback.format_exc(ss))
      print ss
    finally:
      os.chdir(old_cwd)




