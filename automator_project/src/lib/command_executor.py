import os
import urllib2
import glob
import re

class CommandExecutor(object):
  def __init__(self, resources, resources_root="",verbose=True):
    self.verbose = verbose
    self.resources_root = resources_root
    self.resources = resources

  def execute_command(self, bundle_vars, command):
    cmd  = command["Code"]
    methodToCall = getattr(self, cmd)
    new_vars = self.replace_vars(bundle_vars, command["Arguments"])
    methodToCall(**new_vars)
  
  def replace_vars(self, bundle_vars, dictionary):
    new_vars = dictionary.copy()
    for key in new_vars.keys():
      for v in bundle_vars:
        token  = "{{"+v["name"]+"}}" 
        if token in new_vars[key]:
          new_vars[key] = new_vars[key].replace(token, v["value"])
    return new_vars
  
  def ensure_resource_is_registered(self, path):
    templ = '\<AndroidResource Include="'+path+'" /\>'      
  
  def delete(self, **kwargs):
    if self.verbose:
      print "START-delete"
      print "\tfilepath", os.path.abspath(kwargs["FilePath"])
      
    os.remove(kwargs["FilePath"])
    
    if self.verbose:
      print "END-delete"
  
  def replace_from_url(self, **kwargs):
    # print os.path.abspath(kwargs["Source"])
    res = None
    try:
      res = [r for r in self.resources if r["rid"]==kwargs["Resource"]][0]
    except Exception, ex:
      raise Exception("resource not found "+kwargs["Resource"], ex)
    loc = os.path.join(self.resources_root,res["url"]).replace('\\', '/')

    if self.verbose:
      print "START-replace-from-url"
      print "\tdestination", os.path.abspath(kwargs["Destination"])
      print "\tsource", loc
      
    f = urllib2.urlopen(loc)
    fh = open(kwargs["Destination"], 'wb')
    fh.write(f.read())
    fh.close()
    if self.verbose:
      print "DONE-replace-from-url"

  def add_from_url(self, **kwargs):
    self.replace_from_url(**kwargs)

  def __replace_string__(self, variables, item):
    for k in variables:
      token =  "{{"+k["name"]+"}}"
      if token in item:
        item = item.replace(token, k["value"])
    return item
  
  def replace_text(self, **kwargs):
    self.__mass_replace__(kwargs["FileMatch"], kwargs["StringMatch"], kwargs["ReplaceWith"])  
  
  def execute_bundle(self, command_bundle, global_vars):
    bundle_vars = []
    if command_bundle.has_key("Variables"):
      bundle_vars = command_bundle["Variables"]
    for gvar in global_vars:
      if len([x for x in bundle_vars if x["name"] == gvar["name"]])==0:
        bundle_vars.append(gvar)
        
    for comm in command_bundle["Operations"]:
      self.execute_command(bundle_vars, comm)

  def __file_replace__(self, fname, pat, s_after):
    # first, see if the pattern is even in the file.
    if self.verbose:
      print "START-file-text-replace"
      print "\tfile: "+fname
    matchset = None
    with open(fname) as f:
      matchset = re.findall(pat, f.read())
      if not matchset:
        if self.verbose:
          print '\tnothing to replace with', str(pat), "with", s_after
          print "END-file-text-replace"
        return # pattern does not occur in file so we are done.
      else:
        if self.verbose:
          print "\tfound "+str(len(matchset))+" textblocks to replace:"
          for k in matchset:
            print "\t\t item:"+k
       
    # pattern is in the file, so perform replace operation.
    if self.verbose:
      print "\tstarting replacement", str(pat), "with", s_after
    with open(fname) as f:
      out_fname = fname + ".tmp"
      out = open(out_fname, "w")
      out.write(re.sub(pat, s_after, f.read(), len(matchset)))
      out.close()
      os.rename(out_fname, fname)
      if self.verbose:
        print "END-file-text-replace"
  
  def __mass_replace__(self, dir_matches, s_match, s_after): 
    pat = re.compile(s_match)
    files_passed = []
    dm = dir_matches.split("|")
    dms = [x.strip() for x in dm ]
    for dir_match in dms:
      for fname in glob.glob(dir_match):
        if not (fname in files_passed):
          files_passed.append(fname)
          self.__file_replace__(fname, pat, s_after)

  
  
  
  
  
  