import os
import json
import traceback
import subprocess
base_settings = {
                 'branch':'master',
                 'user':'user',
                 'mode':'admin'
                }
class Workspace(object):
  current = None
  registered_bundles = []
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
    return 'mode' in self.settings and self.settings['mode'] or 'admin'
  @mode.setter
  def mode(self, value):
    self.settings['mode'] = value
    self.save()
  
  @property
  def name(self):
    return 'name' in self.settings and self.settings['name'] or ''
  
  @name.setter
  def name(self, value):
    self.settings['name'] = value
    self.save()
  @property
  def plugin_dirs(self):
    return 'plugin_dirs' in self.settings and self.settings['plugin_dirs'] or []
  
  @plugin_dirs.setter
  def plugin_dirs(self, value):
    self.settings['plugin_dirs'] = value
    
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
    if isinstance(command, str):
      cmd = command.split(' ')
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE,
                       close_fds=True, env=os.environ)
    output = []
    for line in iter(p.stdout.readline, b''):
      output.append(line[:-1])
      if just_print:
        if self.loger:
          self.loger.write(line)
        print(line)
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
      print(ss)
    finally:
      os.chdir(old_cwd)

  def configurations(self, **kwargs):
    for root, _, files in os.walk(self.workspacedir):
      for f in files:
        file_path  = os.path.join(root, f)
        if self.is_config_file(file_path):
          yield f

  def is_config_file(self, file_path):
    return file_path.endswith('bc.json') or file_path.endswith('.halc')









