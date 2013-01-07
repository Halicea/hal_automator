'''
Created on Nov 26, 2012

@author: kostamihajlov
'''
import copy
__op_templates ={
  "replace_text":{
    "Code": "replace_text",
    "Description":None,
    "Arguments": {
      "FileMatch": None,
      "StringMatch": None,
      "ReplaceWith": None
    }  
  },
  "replace_from_url":{
    "Code": "replace_from_url",
    "Description": None,
    "Arguments": {
        "Resource": None,
        "Destination": None
    }  
  }
}

def new_operation(code):
  if __op_templates.has_key(code):
    return copy.deepcopy(__op_templates[code])
  else:
    raise NotImplementedError("Operation not supported")

def get_operation_codes():
  return __op_templates.keys()