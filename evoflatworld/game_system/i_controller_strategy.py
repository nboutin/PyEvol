'''
Created on Aug 8, 2019

@author: nboutin
'''


class IControllerStrategy():
    '''
    This an interface.
    Method update must be implemented by subclasses.
    '''

    def update(self, i_game_entity):
        raise NotImplementedError()
