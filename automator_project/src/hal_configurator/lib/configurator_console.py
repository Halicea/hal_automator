#!/usr/bin/env python
# encoding: utf-8
import sys
import os
import json
from hal_configurator.lib.command_executor import CommandExecutor
from hal_configurator.lib.config_loaders import FileConfigLoader, SvcConfigLoader
from hal_configurator.lib.app_prebuilder import AppConfigurator
from hal_configurator.lib.logers import ConsoleLoger, FileLoger, CompositeLoger

svcUrl = "http://localhost:3000"

def main():
  config_loader = get_config_loader()
  custom_bundles = get_additional_bundles()
  custom_vars = get_additional_vars()
  if custom_bundles:
    config_loader.append_bundles(*custom_bundles)
  if custom_vars:
    config_loader.append_vars(*custom_vars)
  builder = AppConfigurator(config_loader, get_logger(), verbose=is_verbose(), debug_mode=False)
  if "-dir" in sys.argv:
    builder.set_execution_dir(sys.argv[sys.argv.index("-dir") + 1])
  builder.apply()
  
def get_additional_bundles():
  custom_bundle = []
  if "-custom-bundle" in sys.argv:
    ind = sys.argv.index("-custom-bundle")+1
    bundlestring = sys.argv[ind]
    custom_bundle = json.loads(bundlestring)
    
  return custom_bundle

def get_additional_vars():
  custom_vars =[]
  if "-custom-vars" in sys.argv:
    ind = sys.argv.index("-custom-vars")+1
    vars_string = sys.argv[ind]
    custom_vars = json.loads(vars_string)
    if not isinstance(custom_vars, list):
      custom_vars = [custom_vars]
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
    config = None
    ldr = None
    base_path = ""
    if sys.argv[2]== 'fs':
      ldr = FileConfigLoader(sys.argv[3])
      res_dir = os.path.abspath(os.path.dirname(sys.argv[3]))
      base_path ="file://"+res_dir
    elif sys.argv[2]=='svc':
      ldr =  SvcConfigLoader(svcUrl, sys.argv[3])
      base_path = os.path.join(svcUrl,"config", sys.argv[3])
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
  if sys.argv[1]=="testLocal":
    __testLocal__()
  elif sys.argv[1]=="testRemote":
    __testRemote__()
  else:
    main()
  print "Done"
