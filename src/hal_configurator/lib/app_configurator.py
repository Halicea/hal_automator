import os
import re
from copy import deepcopy
from hal_configurator.lib.config_validator import ConfigurationValidator
from hal_configurator.lib.workspace_manager import Workspace
from hal_configurator.lib.command_executor import CommandExecutor
from hal_configurator.lib.models.build_filter import ConfigBuildFilter


class AppConfigurator(object):

    def __init__(
            self, config_loader, logger, executor=None,
            verbose=True, debug_mode=True, **kwargs):
        """
        The root execution class, using the apply method
        it runs certain configuration
        against specified execution directory
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
        self.bundles_filter = None
        if 'bundles_filter' in kwargs:
            self.bundles_filter = kwargs['bundles_filter']
        else:
            reg_bundles = ConfigBuildFilter(Workspace.registered_bundles)
            self.bundles_filter = reg_bundles
        self.operations_filter = 'operations_filter' in kwargs and kwargs[
            'operations_filter'] or ConfigBuildFilter()
        self.old_dir = None
        self.validator = ConfigurationValidator(self.config_loader.config_file)
        if self.executor:
            self.executor.parent = self
            self.executors.append(self.executor)

    def release_executor(self, executor):
        """
        removes the execution from the builders executors list
        :param executor:
        """
        self.executors.remove(executor)

    def get_config(self):
        if self.config:
            return self.config
        else:
            self.config = self.config_loader.load_config()
            print("config loaded")
        return self.config

    def apply(self):
        try:
            print "started execution"
            self.old_dir = os.getcwd()
            exec_dir = os.path.abspath(self.get_execution_dir())
            cnf = self.get_config()
            if self.executor is None:
                self.executor = self.create_executor()
            validation_result = self.validator.validate(
                self.get_config(), exec_dir)
            if validation_result.errors or self.verbose:
                self.executor.log.write(repr(validation_result))

            if validation_result.is_valid:
                os.chdir(exec_dir)
                self.configure(cnf, self.executor)
            else:
                os.chdir(self.old_dir)
                # self.executor.log.close()
                raise Exception(
                    'Inavlid Configuration cannot continue with the build')
        finally:
            # self.executor.log.close()
            print "finished execution"
            os.chdir(self.old_dir)

    def apply_parametrized(
            self, config, working_dir=None, selector=True,
            bundles_filter=None, operations_filter=None, **executor_kwargs):
        """
        Runs a custom configuration against a custom working directory
        :param config:
        :type config: dict
        :param working_dir:
        :type working_dir:str
        :param executor_kwargs: **
        """
        print "started execution"
        old_dir = os.getcwd()
        if self.old_dir:
            os.chdir(self.old_dir)

        wd = working_dir or self.get_execution_dir()
        wd = os.path.abspath(wd)
        os.chdir(wd)
        executor = self.create_executor(config=config, **executor_kwargs)
        validation_result = self.validator.validate(self.config, wd)
        if validation_result.errors or self.verbose:
            executor.log.write(repr(validation_result))

        if validation_result.is_valid:
            self.configure(config, executor, bundles_filter=bundles_filter)
        else:
            os.chdir(self.old_dir)
            raise Exception(
                'Invalid Configuration cannot continue with the build')
        print "finished execution"
        os.chdir(old_dir)

    def get_execution_dir(self):
        return self._execution_dir and self._execution_dir or os.getcwd()

    def set_execution_dir(self, execution_dir):
        self._execution_dir = execution_dir

    def exclude_bundles(self, bundles):
        map(self.exclude_bundle, bundles)

    def include_bundles(self, bundles):
        map(self.include_bundle, bundles)

    def include_bundle(self, bundle):
        if isinstance(bundle, dict):
            self.bundles_filter.included.append(bundle['Name'])
        else:
            self.bundles_filter.included.append(bundle)

    def exclude_bundle(self, bundle):
        if isinstance(bundle, dict):
            self.bundles_filter.excluded.append(bundle['Name'])
        else:
            self.bundles_filter.excluded.append(bundle)

    def synthesized_value(self, kvar, global_vars):
        search_pattern = "\{\{\w+\}\}"
        if "{{" in kvar["value"] and "}}" in kvar["value"]:
            val = kvar["value"]
            res = re.findall(search_pattern, val)
            for k in res:
                inner_var = [x for x in global_vars if x["name"] == k[2:-2]]
                if len(inner_var) == 0:

                    print "Variable %s cannot be found" % k
                    available_vars = [x['name'] for x in global_vars]
                    print "Available Variables"
                    print available_vars
                else:
                    inner_var = inner_var[0]
                syth_val = self.synthesized_value(inner_var, global_vars)
                val = val.replace(k, syth_val)

            return val
        else:
            return kvar["value"]

    def configure(
            self, cnf, executor, selector=True,
            bundles_filter=None, operations_filter=None):

        _executor = executor or self.executor
        _bundles_filter = bundles_filter or self.bundles_filter
        _operations_filter = operations_filter or self.operations_filter

        global_vars = []
        if 'Variables' in cnf:
            global_vars = deepcopy(cnf["Variables"])
        global_resources = []
        if 'Resources' in cnf:
            global_resources = deepcopy(cnf["Resources"])

        for k in global_vars:
            k["value"] = self.synthesized_value(k, global_vars)

        if selector is True:
            for bundle in cnf["Content"]["OperationBundles"]:
                if _bundles_filter.allowed(bundle['Name']):
                    _executor.execute_bundle(
                        bundle, global_vars,
                        global_resources, _operations_filter)
                else:
                    if self.verbose:
                        self.logger.write("=" * 20)
                        self.logger.write('SKIPPED %s' % bundle['Name'])
                        self.logger.write("=" * 20)

    def create_executor(self, config=None, logger=None, resources_root=None):
        """
        Creates new Executor for specific config
        :param config:
        :type config: dict
        :param logger:
        :type logger: LoggerBase
        :param resources_root:
        :type resources_root: str
        :return: constructs a Command executor
        :rtype: CommandExecutor
        """
        loader = self.config_loader
        _config = config or self.config
        _log = logger or self.logger

        _resources_root = resources_root or loader.resource_root_url
        root_url = _resources_root
        if os.name != 'posix':
            root_url = "/" + root_url
        root_url = "file://" + root_url
        return CommandExecutor(
            parent=self,
            resources=_config["Resources"],
            resources_root=root_url,
            verbose=self.verbose,
            debug_mode=self.debug_mode,
            log=_log
        )
