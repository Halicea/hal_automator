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


def main(args=None, loger=None):
  if not args:
    args = sys.argv
  config_loader = get_config_loader(args)
  Workspace.set(os.path.dirname(config_loader.config_file))
  custom_bundles = get_additional_bundles(args)
  custom_vars = get_additional_vars(args)
  if custom_bundles:
    config_loader.append_bundles(*custom_bundles)
  if custom_vars:
    config_loader.append_vars(*custom_vars)
  is_outside_loger = True
  if not loger:
    is_outside_loger = False
    loger = get_logger(args)
  builder = AppConfigurator(config_loader, loger, verbose=is_verbose(args), debug_mode=False)
  execution_dir = None
  if "-dir" in args:
    execution_dir = args[args.index("-dir") + 1]
    ex_dir_expanded = os.path.abspath(os.path.expanduser(execution_dir))
    builder.set_execution_dir(ex_dir_expanded)
  validator = ConfigurationValidator(config_loader.config_file)
  validation_result = validator.validate(config_loader.load_config(), ex_dir_expanded)

  if validation_result.is_valid:
    builder.exclude_bundles(get_excluded_bundles(args))
    builder.include_bundles(get_included_bundles(args))
    builder.apply()
    if not is_outside_loger:
      builder.logger.close()
  else:
    builder.logger.write(str(validation_result))
    if not is_outside_loger:
      builder.logger.close()

def get_excluded_bundles(args):
  if "-excluded-bundles" in args:
    ind = args.index("-excluded-bundles")+1
    excbundlestring = args[ind]
    excluded_bundles = json.loads(excbundlestring)
    return excluded_bundles
  return []
def get_included_bundles(args):
  if "-included-bundles" in args:
    ind = args.index("--included-bundles")+1
    incbundlestring = args[ind]
    included_bundles = json.loads(incbundlestring)
    return included_bundles
  return []
def get_additional_bundles(args):
  custom_bundle = []
  if "-custom-bundle" in args:
    ind = args.index("-custom-bundle")+1
    bundlestring = args[ind]
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
    print(("Custom Variables:", custom_vars))
  return custom_vars


def get_logger(args):
  logger = ConsoleLoger()
  if "-log" in args:
    file_log = FileLoger(args[args.index("-log") + 1])
    logger = CompositeLoger(logger, file_log)
  return logger


def is_verbose(args):
  verbose = False
  if "-v" in args:
    verbose = True
  return verbose


def get_config_loader(args):
  if args[1]=='-from':
    ldr = None
    if args[2]== 'fs':
      ldr = FileConfigLoader(args[3])
    elif args[2]=='svc':
      ldr =  SvcConfigLoader(svcUrl, args[3])
    return ldr
  else:
    print('''
    1. automator -from svc [configuration_id] -o [destinationDir]
    2. automator -from fs [configuration_path] -o [destinationDir]
    ''')
    raise Exception("""Console mode requires a ConfigLoader to be specified:+)
    1. automator -from svc [configuration_id] -o [destinationDir]
    2. automator -from fs [configuration_path] -o [destinationDir]
    """)

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
  args = sys.argv
  if args[1]=="testVars":
    get_additional_vars(args)
  if args[1]=="testLocal":
    __testLocal__()
  elif args[1]=="testRemote":
    __testRemote__()
  else:
    main(args)
  print("Done")
