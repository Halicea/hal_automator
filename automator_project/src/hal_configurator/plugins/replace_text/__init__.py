
from hal_configurator.lib.command_base import OperationBase, InvalidCommandArgumentsError,\
  ArgumentDescriptor
import re
import glob
import codecs
import os
class ReplaceText(OperationBase):
  """Replaces Text in the Matched Files"""
  code = "replace_text"
  def __init__(self, *args, **kwargs):
    super(ReplaceText, self).__init__(*args, **kwargs)
    self.result = []
    
  def set_args(self, FileMatch=None, StringMatch=None, ReplaceWith=None):
    self.FileMatch = FileMatch
    self.StringMatch = StringMatch
    self.ReplaceWith = ReplaceWith
    self.kwargs["FileMatch"] = self.FileMatch
    self.kwargs["StringMatch"]=self.StringMatch
    self.kwargs["ReplaceWith"]=self.ReplaceWith
  
  def get_result(self):
    return ','.join(self.result)
  
  @classmethod  
  def get_arg_descriptors(cls):
    return [
              ArgumentDescriptor("FileMatch", "Regex to match on wich files we need to apply the replacement", "text"),
              ArgumentDescriptor("StringMatch", "Regex for the string we like to replace", "text"),
              ArgumentDescriptor("ReplaceWith", "The replacement text", "text")
            ]
  
  @classmethod
  def get_name(cls):
    return "Replace Text"
  
  def get_output_descriptor(self):
    return [
            ArgumentDescriptor("out", "Comma separated list of the paths of the replaced files", "text")
            ]
  
  def run(self):
    is_valid, errors =  self.validate_args()
    if is_valid:
      return self.__mass_replace__(self.FileMatch, self.StringMatch, self.ReplaceWith)
    else:
      raise InvalidCommandArgumentsError(' AND '.join(errors))
  
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
  
  def __file_replace__(self, fname, pat, s_after):
    # first, see if the pattern is even in the file.
    if self.verbose:
      self.log.write("START-file-text-replace")
      self.log.write("\tfile: %s"%fname)
    matchset = None
    with open(fname) as f:
      matchset = re.findall(pat, f.read())
      if not matchset:
        if self.verbose:
          self.log.write('\tnothing to replace %s with %s'%(str(pat), s_after))
          self.log.write("END-file-text-replace")
        return # pattern does not occur in file so we are done.
      else:
        self.result.append(fname)
        if self.verbose:
          self.log.write("\tfound "+str(len(matchset))+" textblocks to replace:")
          for k in matchset:
            self.log.write("\t\t item:"+str(k))
       
    # pattern is in the file, so perform replace operation.
    if self.verbose:
      self.log.write("\tstarting replacement %s with %s"%(str(pat), s_after))
    
    with codecs.open( fname, "r", "utf-8" ) as f:
      out_fname = fname + ".tmp"
      out = codecs.open(out_fname, "w", "utf-8")
      replaced = re.sub(pat, s_after.encode('ascii','ignore'), f.read(), len(matchset))
      out.write(replaced)
      out.close()
      os.rename(out_fname, fname)
      if self.verbose:
        self.log.write("END-file-text-replace")

def test_replace():
  f = open("test.txt", "w")
  f.write("test string\n string again")
  f.close()
  rt = ReplaceText()
  rt.set_args(FileMatch="test.txt", StringMatch = "string", ReplaceWith="bla")
  rt.run()
  r = rt.get_result()
  if r == "test.txt":
    print "file matched"
    f = open("test.txt", "r")
    k = f.read()
    f.close()
    if k == "test bla\n bla again":
      print "test passed"
      return True
    else:
      print "failed"
      print k
      return False
  else:
    print "failed, did not match the file"
    return False

if __name__ =='__main__':
  test_replace()
  
  