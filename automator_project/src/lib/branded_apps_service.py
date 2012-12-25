'''
Created on Nov 19, 2012

@author: kostamihajlov
'''
from lib.hal_rest import HalRest
class BrandedAppService(object):
  def __init__(self, address):
    self.address = address
    self.svc = HalRest( address, False)

  configs =  lambda self:self.svc.get_dict(None, "/svc/branded_apps/config")
  config = lambda (self, config_id): self.svc.get_dict(None, '/svc/branded_apps/config/'+config_id)
  publishers = lambda self:self.svc.get_dict(None, "/svc/branded_apps/publishers")
  platforms =  lambda self:self.svc.get_dict(None, "/svc/branded_apps/platforms")
  resource_types =  lambda self:self.svc.get_dict(None, "/svc/branded_apps/resource_types")
  authentication_types =  lambda self:self.svc.get_dict(None, "/svc/branded_apps/authentication_types")
  application_types =  lambda self:self.svc.get_dict(None, "/svc/branded_apps/application_types")  
  
  def config_full(self, config_id):
    return self.svc.execute_request(None, '/svc/branded_apps/config/'+config_id+"/full") 
  
  def config(self, config_id):
    return self.svc.execute_request(None, '/svc/branded_apps/config/'+config_id)
