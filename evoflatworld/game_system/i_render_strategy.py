'''
Created on Aug 1, 2019

@author: nboutin
'''

class IRenderStrategy():
    '''
    This an interface.
    Method render must be implemented by subclasses.
    '''
    
    def render(self, game_entity, render):
        raise NotImplementedError()