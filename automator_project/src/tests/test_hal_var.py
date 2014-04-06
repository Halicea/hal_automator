'''
Created on Apr 5, 2014

@author: Costa Halicea
'''
import unittest
from collections import namedtuple
from hal_configurator.lib.models.hal_var import HalVar


class TestHalVar(unittest.TestCase):

    def setUp(self):
        self.var_values = {
          'value':'test_value',
          'name':'sample_var',
          'display':'Sample Variable',
          'helptext':'Help Text',
          'validators':[1, 2],
          'admin_only':True,
          'required':False,
          'editable':False,
          'group':'Admin',
          'type':'text',
          'is_from_req':True,
          'options':[{'op1':True}]
        }

    def tearDown(self):
        self.var_values = None
        self.test_var = None

    def testHalVarCreation(self):
        self.test_var = HalVar.from_dict(self.var_values)
        for k in self.var_values.keys():
          msg = 'variable %s has value %s and it was set as %s '%(k, self.test_var[k], self.var_values[k])
          self.assertEquals(self.var_values[k], self.test_var[k], msg)

    def testIterationOfTheKeys(self):
      self.test_var = HalVar.from_dict(self.var_values)
      for k in self.test_var.keys():
        msg = 'variable %s has value %s and it was set as %s '%(k, self.test_var[k], self.var_values[k])
        self.assertEquals(self.var_values[k], self.test_var[k], msg)

    def testIteration(self):
      self.test_var = HalVar.from_dict(self.var_values)
      d = dict( [(k, v) for k, v in self.test_var.items()])
      self.assertEquals(len(d.keys()), len(self.var_values.keys()), 'Keys dont match')
      for k in d.keys():
        self.assertTrue(self.var_values.has_key(k), 'Unknown key %s'%k)

    def testToDictionary(self):
      self.test_var = HalVar.from_dict(self.var_values)
      self.assertEquals(len(self.var_values.keys()), len(self.test_var.dictionary.keys()))

    def testDictionarySet(self):
      self.test_var = HalVar()
      for k in self.var_values.keys():
          msg = 'variable %s has value %s and it was set as %s '%(k, self.test_var[k], self.var_values[k])
          self.assertNotEquals(self.var_values[k], self.test_var[k], msg)
      self.test_var.dictionary = self.var_values
      for k in self.var_values.keys():
          msg = 'variable %s has value %s and it was set as %s '%(k, self.test_var[k], self.var_values[k])
          self.assertEquals(self.var_values[k], self.test_var[k], msg)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'TestHalVar.testHalVarCreation', 'TestHalVar.testIterationOfTheKeys']
    unittest.main()

