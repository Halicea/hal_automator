'''
Created on Apr 6, 2014

@author: Costa Halicea
'''
class HalModule(object):
	name = "No Name"
	operations = []
	__init__(self):
		pass

	def add_operation(self, op):
		self.operations.append(op)

	def remove_operation(self, index):
		del self.operations[index]

	@classmethod
  	def from_dict(cls, d):
  		res = HalModule()
  		res.name = if 'name' in d then d['name'] else 'No Name Set'
  		if 'operations' in d:
  			for op in d['operations']:
  				op = 
  		return 

  	@property
  	def dictionary(self):
  		pass