'''
Created on 15 juil. 2019

@author: f24178c
'''
import unittest
from config_nb import Config

class Test(unittest.TestCase):

    def test(self):
        cfg = Config('utest.yaml')

        self.assertEqual(cfg.get('str'), 'str')
        self.assertEqual(cfg.get('decimal'), 123)
        self.assertEqual(cfg.get('float'), 12.34)
        self.assertEqual(cfg.get('path.to.value'), ['v1','v2','v3'])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()