import sys
import plugin_loader  
class CommandExecutor(object):
  def __init__(self, parent, resources, resources_root="",verbose=True, debug_mode = False, log = lambda x:sys.stdout):
    """
    :param parent:
    :type parent: AppConfigurator
    :param resources:
    :type resources: list
    :param resources_root:
    :type resources_root: str
    :param verbose:
    :type verbose:bool
    :param debug_mode:
    :type verbose:bool
    :param log:
    :type log: LoggerBase
    """
    self.parent = parent
    self.verbose = verbose
    self.resources_root = resources_root
    self.resources = resources
    self.debug_mode = debug_mode
    self.log = log

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

    continue_execution = self.check_debug_settings(command_bundle)

    if continue_execution:
      for comm in command_bundle["Operations"]:
        self.execute_command(comm, bundle_vars, bundle_res)

  def execute_bundle_within_current_scope(self, bundle):
    builder = self.parent
    config = {
               "PublisherId": builder.config["PublisherId"], 
               "RequiredVariables": builder.config["RequiredVariables"],
               "Variables": builder.config["Variables"],
               "Resources": builder.config["Resources"],
               "Content":{
                "OperationBundles":[bundle]
               }
             }
    builder.apply_parametrized(config)
    
  def execute_command(self, command, bundle_vars, bundle_res):
    if self.check_debug_settings(command):
      cmd  = command["Code"]
      plugin_cls = plugin_loader.get_plugin_cls(command)
      plugin = plugin_cls(executor=self, variables=bundle_vars, resources=bundle_res,  verbose=self.verbose, log=self.log)
      vars = self.replace_vars(bundle_vars, command["Arguments"])
      vars = self.replace_resources(bundle_res, vars)
      if "Description" in command:
        plugin.description = command["Description"]
      plugin.set_args(**vars)
      plugin.real_run()
  
  def check_debug_settings(self, obj):
    continue_execution = True
    if self.debug_mode:
      if obj.has_key("DebugSettings"):
        if obj["DebugSettings"].has_key("Break"):
          continue_execution = not obj["DebugSettings"]["Break"]
    return continue_execution
