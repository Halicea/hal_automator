#!/usr/bin/env python
# encoding: utf-8
import sys
import os
import json
from hal_configurator.lib.command_executor import CommandExecutor
from hal_configurator.lib.config_loaders import FileConfigLoader, SvcConfigLoader
from hal_configurator.lib.app_prebuilder import AppPreBuilder
from hal_configurator.lib.logers import ConsoleLoger

svcUrl = "http://localhost:3000"

def main():
  config_loader, executor = get_loader_executor()
  custom_bundles = get_additional_bundles()
  custom_vars = get_additional_vars()
  if custom_bundles:
    config_loader.append_bundles(*custom_bundles)
  if custom_vars:
    config_loader.append_vars(*custom_vars)

  builder = AppPreBuilder(config_loader, executor)

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

def get_loader_executor():
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
      
    config = ldr.load_config()
    verbose=False
    if "-v" in sys.argv:
      verbose = True
    print "Executing configurator on:", os.path.abspath('./')
    exc = CommandExecutor(resources=config["Resources"], resources_root=base_path, verbose=verbose, log=ConsoleLoger())
    return ldr, exc
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
  builder = AppPreBuilder(config_loader, executor)
  builder.apply()

def __testRemote__():
  config_loader = SvcConfigLoader(svcUrl, "testConfig")
  executor = CommandExecutor(verbose=True)
  builder = AppPreBuilder(config_loader, executor)
  builder.apply()
            
if __name__ == '__main__':
  if sys.argv[1]=="testLocal":
    __testLocal__()
  elif sys.argv[1]=="testRemote":
    __testRemote__()
  else:
    main()
  print "Done"
