'''
Created on 15 juil. 2019

@author: f24178c
'''

import yaml
import os

class Config():
    def __init__(self, filename):
        
        local_dir = os.path.dirname(__file__)
        pathname = os.path.join(local_dir, filename)

        with open(pathname)  as file:
            self.doc = yaml.safe_load(file)

    def get(self, path):
        """
        :param path, 'key' or 'path.to.key'
        """
        keys = path.split('.')
        r = self.doc
        for k in keys:
            r = r[k]
        return r    

if __name__ == '__main__':
    
    Config('demo.yaml')
