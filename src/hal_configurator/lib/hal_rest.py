#!/usr/bin/env python
# encoding: utf-8
"""
prinstand_integration_tests.py
Created by Kosta Mihajlov on 2012-07-19.
Copyright (c) 2012 Halicea.Co. All rights reserved.
"""
import datetime
import json
import requests
verbose = True
address = None
def run_tests(title, test_address, tests_dict):
  global address  
  print(test_address)
  address = test_address  
  print(("="*len(title)))
  print(title)
  print(("="*len(title)))
  print()
  print(("  Generated On: :: ", datetime.date.today())) 
  print()
  for k in tests_dict:
    print((k[0]))
    print(("="*len(k[0])))
    print() 
    k[1]()
    print()
def set_address(add):
  global address
  address = add

def execute_request(token, selector, headers={}, method="GET", data="", attachment=None):
  req = method=="POST" and requests.post or requests.get   
  print(address)
  res = req(address+selector,data=data, cookies={"mwr.sid":token}, headers=headers, files =  attachment and {'attachment':attachment} or None) 
  if verbose:
    print()
    print("Request")
    print("+++++++")
    print()
    print(("  Selector:", selector))
    print()
    print(("  Method:", method))
    print()
    print(("  Data:", data))   
    print()
    print("  Headers: ::")
    print()
    print(("    "+str(headers)))
    print()
    print("Response:")
    print("+++++++++")   
    print()
    print(("  Status:", res.status_code))    
    print()
    print("  Headers: ::")        
    print() 
    print(('    '+str(res.headers)))
    print()
    print("  Response Content:  ::") 
    print() 
    print((''.join(['     '+x+'\n' for x in res.text.split('\n')] )))
  return res.text, res.status_code   
class RestException(Exception):
  def __init__(self, message=""):
    super(RestException, self).__init__(message=message)

class HalRest(object): 
  """docstring for ClassName"""
  def __init__(self, address, verbose=True):
    super(HalRest, self).__init__()       
    self.verbose = verbose
    self.address = address 
    
  def execute_request(self, token, selector, headers={}, method="GET", data="", attachment=None):
    req = method=="POST" and requests.post or requests.get   
    #print self.address
    res = req(self.address+selector,data=data, cookies={"mwr.sid":token}, headers=headers, files =  attachment and {'attachment':attachment} or None) 
    if self.verbose:
      print()
      print("Request")
      print("+++++++")
      print()
      print(("  Selector:", selector))
      print()
      print(("  Method:", method))
      print()
      print(("  Data:", data))   
      print()
      print("  Headers: ::")
      print()
      print(("    "+str(headers)))
      print()
      print("Response:")
      print("+++++++++")   
      print()
      print(("  Status:", res.status_code))    
      print()
      print("  Headers: ::")        
      print() 
      print(('    '+str(res.headers)))
      print()
      print("  Response Content:  ::") 
      print() 
      print((''.join(['     '+x+'\n' for x in res.text.split('\n')] )))
    return res.text, res.status_code 

  def get_dict(self, token, selector, headers={}, method="GET", data="", f=None):
    status, res = self.execute_request(token, selector, headers, method, data, f)
    if status =="ok":
      res = json.loads(res)
      if res["data"]:
        return res["data"]
      else:
        raise RestException        