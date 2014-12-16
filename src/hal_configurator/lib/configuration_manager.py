'''
Created on Jan 7, 2013

@author: kostamihajlov
'''
class InvalidConfigurationError(Exception):
  pass
  
class ConfigurationManager(object):
  
  def __init__(self, service_address):
    self.service_address = service_address
  
  def upload_config(self, config_path):
    if self._validate():
      zip_path = self._compress_config(config_path)
      response = self._upload(zip_path)
      return response["status"]=="ok"
    else:
      raise InvalidConfigurationError()
  
  def _validate(self, config_path):
    raise NotImplementedError()
    
  def download_config(self, config_id, destination_dir):
    self._download(config_id)
    
  def _download(self, config_id):
    raise NotImplementedError()
  
  def _upload(self,compressed_config):
    raise NotImplementedError()
  
  def _compress_config(self, config_path):
    raise NotImplementedError()
  
  def _decompress_config(self, zip_path):
    raise NotImplementedError()
