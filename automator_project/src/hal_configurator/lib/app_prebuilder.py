import os
import urllib
from hal_configurator.lib.command_executor import CommandExecutor


class AppConfigurator(object):
  def __init__(self, config_loader, logger ,executor=None, verbose=True, debug_mode=True):
    """

    :param config_loader:
    :type config_loader ConfigLoader
    :param logger: LoggerBase
    :param executor:
    :type executor CommandExecutor
    :param verbose:
    :type verbose: bool
    :param debug_mode:
    :type debug_mode: bool
    """
    self.config_loader = config_loader
    self.logger = logger
    self.debug_mode = debug_mode
    self.verbose = verbose
    self.executor = executor
    self.config = None
    self._execution_dir = None
    self.executors = []
    if self.executor:
      self.executor.parent = self
      self.executors.append(self.executor)

  def release_executor(self, executor):
    self.executors.remove(executor)

  def get_config(self):
    print "in configure"
    if self.config:
      print "returning config"
      return self.config
    else:
      self.config = self.config_loader.load_config()
      print "config loaded"
    return self.config

  def apply(self):
    print "started execution"
    old_dir = os.getcwd()
    os.chdir(self.get_execution_dir())
    cnf = self.get_config()
    if self.executor is None:
      self.executor = self.create_executor()
    self.configure(cnf, self.executor)
    self.executor.log.close()
    print "finished execution"
    os.chdir(old_dir)

  def apply_parametrized(self, config, working_dir=None, **executor_kwargs):
    """

    :param config:
    :type config: dict
    :param working_dir:
    :type working_dir:str
    :param executor_kwargs: **
    """
    print "started execution"
    wd = working_dir or self.get_execution_dir()
    old_dir = os.getcwd()
    os.chdir(wd)
    executor = self.create_executor(config=config, **executor_kwargs)
    self.configure(config, executor)
    self.executor.log.close()
    print "finished execution"
    os.chdir(old_dir)

  def get_execution_dir(self):
    return self._execution_dir and self._execution_dir or os.getcwd()

  def set_execution_dir(self, execution_dir):
    self._execution_dir = execution_dir

  def configure(self, cnf, executor, selector=True):
    _executor = executor or self.executor
    global_vars=[]
    if cnf.has_key("Variables"):
      global_vars = cnf["Variables"]
    global_resources = []
    if cnf.has_key("Resources"):
      global_resources = cnf["Resources"]
    if selector is True:
      for bundle in cnf["Content"]["OperationBundles"]:
        _executor.execute_bundle(bundle, global_vars, global_resources)

  def create_executor(self, config = None, logger=None, resources_root=None):
    _config = config or self.config
    _log = logger or self.logger
    _resources_root = resources_root or self.config_loader.resource_root_url
    root_url = urllib.pathname2url(_resources_root)
    if os.name != 'posix':
      root_url="/"+root_url
    root_url= "file://"+root_url
    return CommandExecutor(
      parent = self,
      resources=_config["Resources"],
      resources_root=root_url,
      verbose=self.verbose,
      debug_mode=self.debug_mode,
      log=_log
    )