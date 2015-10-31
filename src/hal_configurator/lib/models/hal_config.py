'''
Created on Apr 6, 2014

@author: Costa Halicea
'''
class ConfigDefintion(object):
	Modules = []

	@classmethod
  	def from_dict(cls, d):
  		res = HalModule()
  		res.name = if 'name' in d then d['name'] else 'No Name Set'
  		if 'operations' in d:
  			for op in d['operations']:
  				op = 

class Config(object):
	References = {}
	Builds = None
	
	Definition = None

	Variables = []
	Resources = []

	RequiredVariables = None
	RequiredResources = None

	def __init__(self):
		self.References = {}
		self.Builds = []
		self.Definition = ConfigDefintion()
		self.Variables = []
		self.RequiredVariables = []
		self.RequiredResources = []


	@classmethod
	def from_dict(cls, d):
		res = Config()
		if 'Content' in d:
			self.
	
	@staticmethod
	def __validate_dict__(d)
		errors = []
		if 'Builds' in d and not isinstance(d['Builds'], list):
			errors.append({'key':'References', 'message':'Builds should be an array'})
		
		if 'Definition' in d and not isinstance(d['Builds']):
			errors.append({'key':'References', 'message':'Builds should be an array'})



	@property
	def dictionary(self):
		pass