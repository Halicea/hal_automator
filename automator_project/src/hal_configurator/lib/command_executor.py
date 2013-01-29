import os
import urllib2
import glob
import re
import codecs
import hal_configurator.plugins as plugins

class CommandExecutor(object):
  def __init__(self, resources, resources_root="",verbose=True):
    self.verbose = verbose
    self.resources_root = resources_root
    self.resources = resources

  def replace_vars(self, bundle_vars, dictionary):
    new_vars = dictionary.copy()
    for key in new_vars.keys():
      for v in bundle_vars:
        token  = "{{"+v["name"]+"}}"
        if token in new_vars[key]:
          new_vars[key] = new_vars[key].replace(token, v["value"])
    return new_vars
  
  def replace_resources(self, bundle_res, dictionary):
    new_vars = dictionary.copy()
    for key in new_vars.keys():
      for r in bundle_res:
        token  = "{#"+r["rid"]+"#}"
        if token in new_vars[key]:
          new_vars[key] = new_vars[key].replace(token, r["url"])
    return new_vars
  
  def execute_bundle(self, command_bundle, global_vars, global_resources):
    bundle_vars = []
    if command_bundle.has_key("Variables"):
      bundle_vars = command_bundle["Variables"]
    
    for gvar in global_vars:
      if len([x for x in bundle_vars if x["name"] == gvar["name"]])==0:
        bundle_vars.append(gvar)
    
    bundle_res = []
    if command_bundle.has_key("Resources"):
      bundle_res = command_bundle["Resources"] 
    for gres in global_resources:
      if len([x for x in bundle_res if x["rid"] == gres["rid"]])==0:
        bundle_res.append(gres)
        
    for k in bundle_res:
      if not ("://" in k["url"]):
        k["url"] = self.resources_root+"/"+k["url"]
    
    for comm in command_bundle["Operations"]:
      self.execute_command(comm, bundle_vars, bundle_res)
    
  def execute_command(self, command, bundle_vars, bundle_res):
    vars = self.replace_vars(bundle_vars, command["Arguments"])
    vars = self.replace_resources(bundle_res, vars)
    
    
    cmd  = command["Code"]
    plugin_cls = plugins.__dict__[cmd]
    
    plugin = plugin_cls(executor = self, variables = bundle_vars, resources = bundle_res,  verbose=True)
    plugin.set_args(**vars)
    plugin.run()