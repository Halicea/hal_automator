'''
Created on Apr 5, 2014

@author: Costa Halicea
'''
import unittest
from hal_configurator.lib.models.hal_var import HalResource


class TestHalResource(unittest.TestCase):

    def setUp(self):
        self.res_values = {
          'rid':'test_value',
          'url':'sample_res',
          'display':'Sample resource',
          'helptext':'Help Text',
          'validators':[1, 2],
          'admin_only':True,
          'required':False,
          'editable':False,
          'group':'Admin',
          'type':'text',
          'is_from_req':True
        }

    def tearDown(self):
        self.res_values = None
        self.test_res = None

    def testHalResourceCreation(self):
        self.test_res = HalResource.from_dict(self.res_values)
        for k in self.res_values.keys():
          msg = 'resource %s has value %s and it was set as %s '%(k, self.test_res[k], self.res_values[k])
          self.assertEquals(self.res_values[k], self.test_res[k], msg)

    def testIterationOfTheKeys(self):
      self.test_res = HalResource.from_dict(self.res_values)
      for k in self.test_res.keys():
        msg = 'resource %s has value %s and it was set as %s '%(k, self.test_res[k], self.res_values[k])
        self.assertEquals(self.res_values[k], self.test_res[k], msg)

    def testIteration(self):
      self.test_res = HalResource.from_dict(self.res_values)
      d = dict( [(k, v) for k, v in self.test_res.items()])
      self.assertEquals(len(d.keys()), len(self.res_values.keys()), 'Keys dont match')
      for k in d.keys():
        self.assertTrue(self.res_values.has_key(k), 'Unknown key %s'%k)

    def testToDictionary(self):
      self.test_res = HalResource.from_dict(self.res_values)
      self.assertEquals(len(self.res_values.keys()), len(self.test_res.dictionary.keys()))

    def testDictionarySet(self):
      self.test_res = HalResource()
      for k in self.res_values.keys():
          msg = 'resource %s has value %s and it was set as %s '%(k, self.test_res[k], self.res_values[k])
          self.assertNotEquals(self.res_values[k], self.test_res[k], msg)
      self.test_res.dictionary = self.res_values
      for k in self.res_values.keys():
          msg = 'resource %s has value %s and it was set as %s '%(k, self.test_res[k], self.res_values[k])
          self.assertEquals(self.res_values[k], self.test_res[k], msg)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'TestHalResource.testHalResourceCreation', 'TestHalResource.testIterationOfTheKeys']
    unittest.main()

