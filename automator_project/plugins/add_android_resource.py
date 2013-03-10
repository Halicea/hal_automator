from hal_configurator.lib.command_base import OperationBase, ArgumentDescriptor, InvalidCommandArgumentsError
from replace_from_url import ReplaceFromUrl as replace_from_url
from replace_text import ReplaceText as replace_text

__author__ = 'Costa Halicea'

class AddAndroidResource(OperationBase):
  """Replaces File(Destination) from a resource file supplied by URI"""
  def __init__(self,*args, **kwargs):
    super(AddAndroidResource, self).__init__(*args, **kwargs)
    self.result = ''

  @classmethod
  def get_arg_descriptors(cls):
    return [
            ArgumentDescriptor("ResourceFormat", "The Resource to use", "text"),
            ArgumentDescriptor("DestinationFormat", "Where to put the file(relative to the working dir or absolute)", "text"),
            ArgumentDescriptor("IteratorArray", "Iterator for the Resources", "text"),
            ArgumentDescriptor("ProjectFile", "ProjectFilePath", "text")
           ]

  def set_args(self, ResourceFormat, DestinationFormat, IteratorArray, ProjectFile):
    self.kwargs["ProjectFile"]=self.project_file = ProjectFile
    self.kwargs["ResourceFormat"]= self.resource_format = ResourceFormat
    self.kwargs["DestinationFormat"]= self.destination_format = DestinationFormat
    self.kwargs["IteratorArray"] = DestinationFormat
    self.iterator_array = IteratorArray.split(",")

  def run(self):
    is_valid, errors = self.validate_args()
    if is_valid:
      for k in self.iterator_array:
        res = self.resource_format%k
        dest = self.destination_format%k
        res = self.value_substitutor.substitute(res)
        dest = self.value_substitutor.substitute(dest)
        rurl = replace_from_url(executor = self.executor,
                                resources = self.resources,
                                variables = self.variables,
                                verbose=self.verbose)

        rtext= replace_text(executor = self.executor,
                            resources = self.resources,
                            variables = self.variables,
                            verbose=self.verbose)
        match = "</Project>$"
        repl = "<ItemGroup><AndroidResource Include=\""+dest.replace('/', "\\\\")+"\" /></ItemGroup>\n</Project>"
        rurl.set_args(res, dest)
        rtext.set_args(self.project_file, match, repl)
        rurl.run()
        rtext.run()
    else:
      raise InvalidCommandArgumentsError(str(errors))

__plugin__ = AddAndroidResource