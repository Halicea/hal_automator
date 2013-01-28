import os
from hal_configurator.lib.command_base import OperationBase, ArgumentDescriptor

class Operation(OperationBase):
  def __init__(self):
    pass
  def get_arg_descriptors(self):
    return [
            ArgumentDescriptor("FilePath", "The absolute file path of the file to be deleted", "text", os.path.exists)
            ]
    
  def run(self, **kwargs):
    if self.verbose:
      print "START-delete"
      print "\tfilepath", os.path.abspath(kwargs["FilePath"])
      
    os.remove(kwargs["FilePath"])
    
    if self.verbose:
      print "END-delete"
      
class ProjectResourcesAppender(OperationBase):
  def __init__(self):
    pass
  
  def get_arg_descriptors(self):
    return [
            ArgumentDescriptor("ProjectFile", "The absolute file path of the Project file", "text", os.path.exists),
            ArgumentDescriptor("ResourceDestinationFormat", "Where the resource will be saved", "text", lambda x: "%s" in x),
            ArgumentDescriptor("ResourceFormat", "Which Resource are we chosing to be added", "text", lambda x: "%s" in x),
            ArgumentDescriptor("ReplacementArray", "Comma delimited array of values for replacement(no whitespaces between)", "text", None)
            ]
    
  def run(self, **kwargs):
    repl_with = "<ItemGroup><AndroidResource Include=\"%s\"/></ItemGroup>\n</Project>"
    str_match = "^\</Project\>"
    file_match = kwargs["ProjectFile"]
    res_format = kwargs["ResourceDestinationFormat"]
    res = kwargs["ResourceFormat"]
    replacement_array = kwargs["ReplacementArray"].split(",")
    
    for k in replacement_array:
      self.replace_text(FileMatch=file_match, StringMatch=str_match, ReplaceWith=repl_with%(res_format%k,))
      self.replace_from_url(res_format%k, res%k)
