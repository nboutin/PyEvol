'''
Created on Aug 8, 2019

@author: nboutin
'''


class IController():
    '''
    This an interface.
    Method update must be implemented by subclasses.
    '''

    def update(self, i_game_entity):
        raise NotImplementedError()
