#!/usr/bin/env python
# encoding: utf-8
import sys
import os
import json
from hal_configurator.lib.command_executor import CommandExecutor
from hal_configurator.lib.config_loaders import FileConfigLoader, SvcConfigLoader
from hal_configurator.lib.app_configurator import AppConfigurator
from hal_configurator.lib.logers import ConsoleLoger, FileLoger, CompositeLoger
import hal_configurator.lib.app_config as app_config
from hal_configurator.lib.config_validator import ConfigurationValidator
from hal_configurator.lib.workspace_manager import Workspace
svcUrl = "http://localhost:3000"


def main():
  print "Starting Configurator"
  print "Version", app_config.get_version()
  config_loader = get_config_loader()
  Workspace.set(os.path.dirname(config_loader.config_file))
  custom_bundles = get_additional_bundles()
  custom_vars = get_additional_vars(sys.argv)
  if custom_bundles:
    config_loader.append_bundles(*custom_bundles)
  if custom_vars:
    config_loader.append_vars(*custom_vars)

  builder = AppConfigurator(config_loader, get_logger(), verbose=is_verbose(), debug_mode=False)
  execution_dir = None
  if "-dir" in sys.argv:
    execution_dir = sys.argv[sys.argv.index("-dir") + 1]
    ex_dir_expanded = os.path.abspath(os.path.expanduser(execution_dir))
    builder.set_execution_dir(ex_dir_expanded)
  validator = ConfigurationValidator(config_loader.config_file)
  validation_result = validator.validate(config_loader.load_config(), ex_dir_expanded)

  if validation_result.is_valid:
    builder.exclude_bundles(get_excluded_bundles())
    builder.include_bundles(get_included_bundles())
    builder.apply()
    builder.logger.close()
  else:
    builder.logger.write(str(validation_result))
    builder.logger.close()
    sys.exit(1)

def get_excluded_bundles():
  if "-excluded-bundles" in sys.argv:
    ind = sys.argv.index("-excluded-bundles")+1
    excbundlestring = sys.argv[ind]
    excluded_bundles = json.loads(excbundlestring)
    return excluded_bundles
  return []
def get_included_bundles():
  if "-included-bundles" in sys.argv:
    ind = sys.argv.index("--included-bundles")+1
    incbundlestring = sys.argv[ind]
    included_bundles = json.loads(incbundlestring)
    return included_bundles
  return []
def get_additional_bundles():
  custom_bundle = []
  if "-custom-bundle" in sys.argv:
    ind = sys.argv.index("-custom-bundle")+1
    bundlestring = sys.argv[ind]
    custom_bundle = json.loads(bundlestring)
  return custom_bundle

def get_additional_vars(args):
  custom_vars =[]
  if "-custom-vars" in args:
    ind = args.index("-custom-vars")+1
    custom_vars = []
    for k in args[ind:]:
      if '=' in k:
        kar = k.split('=')
        v = {"name":kar[0], "value":kar[1]}
        custom_vars.append(v)
      else:
        break
    print "Custom Variables:", custom_vars
  return custom_vars


def get_logger():
  logger = ConsoleLoger()
  if "-log" in sys.argv:
    file_log = FileLoger(sys.argv[sys.argv.index("-log") + 1])
    logger = CompositeLoger(logger, file_log)
  return logger


def is_verbose():
  verbose = False
  if "-v" in sys.argv:
    verbose = True
  return verbose


def get_config_loader():
  if sys.argv[1]=='-from':
    ldr = None
    if sys.argv[2]== 'fs':
      ldr = FileConfigLoader(sys.argv[3])
    elif sys.argv[2]=='svc':
      ldr =  SvcConfigLoader(svcUrl, sys.argv[3])
    return ldr
  else:
    print '''
    1. t2sconf -from svc [configuration_id] -o [destinationDir]
    2. t2sconf -from fs [configuration_path] -o [destinationDir]
    '''
    #raise Exception("Invalid Parameters")

def __testLocal__():
  workingDir =os.path.dirname(os.path.abspath(__file__))
  config_loader = FileConfigLoader("../test_data/build_configuration.json")
  config = config_loader.load_config()
  executor = CommandExecutor(config["Resources"],basePath=workingDir, verbose=True)
  builder = AppConfigurator(config_loader, executor)
  builder.apply()

def __testRemote__():
  config_loader = SvcConfigLoader(svcUrl, "testConfig")
  executor = CommandExecutor(verbose=True)
  builder = AppConfigurator(config_loader, executor)
  builder.apply()

if __name__ == '__main__':
  if sys.argv[1]=="testVars":
    get_additional_vars(sys.argv)
  if sys.argv[1]=="testLocal":
    __testLocal__()
  elif sys.argv[1]=="testRemote":
    __testRemote__()
  else:
    main()
  print "Done"
