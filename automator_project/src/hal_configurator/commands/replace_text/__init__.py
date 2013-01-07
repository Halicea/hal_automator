
from lib.command_base import CommandBase, InvalidCommandArgumentsError
import re
import glob

class ReplaceText(CommandBase):
  """Replaces Text in the Matched Files"""
  def __init__(self, FileMatch=None, StringMatch=None, ReplaceWith=None):
    self.FileMatch = FileMatch
    self.StringMatch = StringMatch
    self.ReplaceWith = ReplaceWith
    errors = self.__validate_input__()
    if errors:
      raise InvalidCommandArgumentsError(' AND '.join(errors))

  def __validate_input__(self):
    error_messages =[]
    if not(self.FileMatch and self.StringMatch and self.ReplaceWith):
      return ["One or more parameters are not supplied"]
    return error_messages
  
  def run(self):
    self.__mass_replace__(self.FileMatch, self.StringMatch, self.ReplaceWith)
  
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
      print "START-file-text-replace"
      
    with open(fname) as f:
      if not any(re.search(pat, line) for line in f):
        if self.verbose:
          print '\tnothing to replace with', str(pat), "with", s_after
          print "END-file-text-replace"
        return # pattern does not occur in file so we are done.
  
      