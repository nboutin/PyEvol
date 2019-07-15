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
    print (cfg.get('badkey', "default value"))

    for m in cfg.message_list:
        print (m,' ',end='')
    print()
        
    print (cfg.str1, '+', cfg.str2,'=',cfg.strconcat)
    print (cfg.value1, '+', cfg.value2, '=', cfg.total)
    
#     Save is not support with Python3
#     save_pathname = os.path.join(local_dir, 'save.cfg')
#     save_file = open(save_pathname, 'w')
#     cfg.save(save_file)
