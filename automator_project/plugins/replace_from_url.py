import urllib2
from hal_configurator.lib.command_base import \
  OperationBase, InvalidCommandArgumentsError, ArgumentDescriptor
class ReplaceFromUrl(OperationBase):
  """Replaces File(Destination) from a resource file supplied by URI"""
  code = "replace_from_url"
  def __init__(self,*args, **kwargs):
    super(ReplaceFromUrl, self).__init__(*args, **kwargs)
    self.result = ''
  
  @classmethod  
  def get_arg_descriptors(cls):
    return [
            ArgumentDescriptor("Resource", "The Resource to use", "text"),
            ArgumentDescriptor("Destination", "Where to put the file(relative to the working dir or absolute)", "text")
            ]
  def set_args(self, Resource, Destination):
    self.kwargs["Resource"]= self.resource = Resource
    self.kwargs["Destination"]= self.destination = Destination

  def run(self):
    is_valid, errors = self.validate_args()
    if is_valid:
      res = self.resource.replace('\\', '/')
      f = urllib2.urlopen(res)
      fh = open(self.destination, 'wb')
      fh.write(f.read())
      fh.close()
    else:
      raise InvalidCommandArgumentsError(str(errors))

__plugin__ = ReplaceFromUrl

def test_replace_from_url():
  rfu = ReplaceFromUrl(verbose=True)
  rfu.set_args()
