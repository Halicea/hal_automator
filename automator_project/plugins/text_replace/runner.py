'''
Created on Jan 11, 2013

@author: kostamihajlov
'''
import re
from hal_configurator.lib.command_base import OperationBase, ArgumentDescriptor ,InvalidCommandArgumentsError

class TextReplace(OperationBase):
  """
  Replaces Text in files that are matched by the FileMatch parameter
  The text is replaced using regex expression
  """
  def __init__(self, *args, **kwargs):
    super(TextReplace, self).__init__(*args, **kwargs)
    
    self.title = "Replace Text"
    self.argument_descriptors = [
        ArgumentDescriptor("FileMatch", "Which Files to replace", "text"),
        ArgumentDescriptor("StringMatch", "Find with", "text"),
        ArgumentDescriptor("ReplaceWith", "Replace With", "text")]
    self.result_descriptor = ArgumentDescriptor(None, None, None)
  
  def get_argument_descriptors(self):
    return self.argument_descriptors 
  
  def get_result_descriptor(self):
    return self.result_descriptor
  
  def run(self, **kwargs):
    pass
  
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
    
    with codecs.open( fname, "r", "utf-8" ) as f:
      out_fname = fname + ".tmp"
      out = codecs.open(out_fname, "w", "utf-8")
      replaced = re.sub(pat, s_after.encode('ascii','ignore'), f.read(), len(matchset))
      out.write(replaced)
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

  
    
