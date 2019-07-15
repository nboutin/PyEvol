'''
Created on 15 juil. 2019

@author: nboutin
'''

from config import Config
import os

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_pathname = os.path.join(local_dir, 'simple.cfg')
    cfg = Config(config_pathname)
    print (cfg)
    print (cfg.message)
