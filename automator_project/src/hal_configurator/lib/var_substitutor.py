class VarSubstitutor(object):

  def __init__(self, variables, resources, resources_root):
    self.variables = variables
    self.resources = resources
    self.resources_root = resources_root

  def substitute_vars(self, string):
    for k in self.variables:
      if "{{"+k["name"]+"}}" in string:
        string = string.replace("{{"+k["name"]+"}}", k["value"])
    return string

  def substitute_resources(self, string):
    for k in self.resources:
      if "{#"+k["rid"]+"#}" in string:
        string  = string.replace("{#"+k["rid"]+"#}", k["url"])
        if not (self.resources_root in string):
          string  = self.resources_root+"/"+string
    return string

  def substitute(self, text):
    t  = self.substitute_vars(text)
    return self.substitute_resources(t)
