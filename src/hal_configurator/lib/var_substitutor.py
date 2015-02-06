import os
from xml.sax.saxutils import escape
class VarSubstitutor(object):

  def __init__(self, variables, resources, resources_root):
    self.variables = variables
    self.resources = resources
    self.resources_root = resources_root

  def substitute_vars(self, string):
    for k in self.variables:
      if '{{'+k['name']+'}}' in string:
        string = string.replace('{{'+k['name']+'}}', k['value'])
    return string

  def substitute_resources(self, string):
    for k in self.resources:
      if '{#'+k['rid']+'#}' in string:
        string = string.replace('{#' + k['rid'] + '#}', k['url'])
        if not (self.resources_root in string):
          string = self.resources_root + '/' + string
    return string

  def substitute_expressions(self, string):
    result = string
    eval_globals = {
        'os': os,
        'xml_escape': escape,
    }
    while "{!" and "!}" in result:
      index_start = string.index('{!') + 2
      index_end = string.index('!}', index_start)

      to_eval = string[index_start:index_end]
      result = result.replace('{!' + to_eval + '!}',
                              str(eval(to_eval, eval_globals)))
    return result

  def substitute(self, text):
    t = self.substitute_vars(text)
    t = self.substitute_resources(t)
    t = self.substitute_expressions(t)
    return t
