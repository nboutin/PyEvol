'''
Created on Aug 20, 2019

@author: nbout
'''

class Food():
    
    def __init__(self):
        print("init food")
        
    def __del__(self):
        print("del food")

if __name__ == '__main__':
    
    l = list()
    
    f = Food()
    l.append(f)
    l.remove(f)
    del f
    print("end")