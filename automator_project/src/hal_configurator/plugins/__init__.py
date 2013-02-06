#from delete_file import DeleteFile 
from replace_text import ReplaceText as replace_text
from replace_from_url import ReplaceFromUrl as replace_from_url
from add_android_resource import AddAndroidResource as add_android_resource
from add_ios_resource import AddIosResource as add_ios_resource

__all__ = ["replace_text", "replace_from_url", "add_android_resource", "add_ios_resource"]

#  def ensure_resource_is_registered(self, path):
#    templ = '\<AndroidResource Include="'+path+'" /\>'      
#  
#  def delete(self, **kwargs):
#    if self.verbose:
#      print "START-delete"
#      print "\tfilepath", os.path.abspath(kwargs["FilePath"])
#      
#    os.remove(kwargs["FilePath"])
#    
#    if self.verbose:
#      print "END-delete"
#  
#  def replace_from_url(self, **kwargs):
#    # print os.path.abspath(kwargs["Source"])
#    res = None
#    try:
#      res = [r for r in self.resources if r["rid"]==kwargs["Resource"]][0]
#    except Exception, ex:
#      raise Exception("resource not found "+kwargs["Resource"], ex)
#    loc = os.path.join(self.resources_root,res["url"]).replace('\\', '/')
#
#    if self.verbose:
#      print "START-replace-from-url"
#      print "\tdestination", os.path.abspath(kwargs["Destination"])
#      print "\tsource", loc
#    f = urllib2.urlopen(loc)
#    fh = open(kwargs["Destination"], 'wb')
#    fh.write(f.read())
#    fh.close()
#    if self.verbose:
#      print "DONE-replace-from-url"
#
#  def add_android_resource(self, **kwargs):
#    repl_with = "<ItemGroup><AndroidResource Include=\"%s\"/></ItemGroup>\n</Project>"
#    str_match = "^\</Project\>"
#    file_match = kwargs["ProjectFile"]
#    res_format = kwargs["ResourceDestinationFormat"]
#    res = kwargs["ResourceFormat"]
#    replacement_array = kwargs["ReplacementArray"].split(",")
#    
#    for k in replacement_array:
#      self.replace_text(FileMatch=file_match, StringMatch=str_match, ReplaceWith=repl_with%(res_format%k,))
#      self.replace_from_url(res_format%k, res%k)
#      
#
#  def add_from_url(self, **kwargs):
#    self.replace_from_url(**kwargs)
#
#  def __replace_string__(self, variables, item):
#    for k in variables:
#      token =  "{{"+k["name"]+"}}"
#      if token in item:
#        item = item.replace(token, k["value"])
#    return item
#  
#  def replace_text(self, **kwargs):
#    self.__mass_replace__(kwargs["FileMatch"], kwargs["StringMatch"], kwargs["ReplaceWith"])  
#  
#  def __file_replace__(self, fname, pat, s_after):
#    # first, see if the pattern is even in the file.
#    if self.verbose:
#      print "START-file-text-replace"
#      print "\tfile: "+fname
#    matchset = None
#    with open(fname) as f:
#      matchset = re.findall(pat, f.read())
#      if not matchset:
#        if self.verbose:
#          print '\tnothing to replace with', str(pat), "with", s_after
#          print "END-file-text-replace"
#        return # pattern does not occur in file so we are done.
#      else:
#        if self.verbose:
#          print "\tfound "+str(len(matchset))+" textblocks to replace:"
#          for k in matchset:
#            print "\t\t item:"+k
#       
#    # pattern is in the file, so perform replace operation.
#    if self.verbose:
#      print "\tstarting replacement", str(pat), "with", s_after
#    
#    with codecs.open( fname, "r", "utf-8" ) as f:
#      out_fname = fname + ".tmp"
#      out = codecs.open(out_fname, "w", "utf-8")
#      replaced = re.sub(pat, s_after.encode('ascii','ignore'), f.read(), len(matchset))
#      out.write(replaced)
#      out.close()
#      os.rename(out_fname, fname)
#      if self.verbose:
#        print "END-file-text-replace"
#
#  def __mass_replace__(self, dir_matches, s_match, s_after): 
#    pat = re.compile(s_match)
#    files_passed = []
#    dm = dir_matches.split("|")
#    dms = [x.strip() for x in dm ]
#    for dir_match in dms:
#      for fname in glob.glob(dir_match):
#        if not (fname in files_passed):
#          files_passed.append(fname)
#          self.__file_replace__(fname, pat, s_after)
