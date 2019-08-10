'''
Created on Aug 1, 2019

@author: nboutin
'''


class IPhysicsStrategy():
    '''
    This an interface.
    Method update must be implemented by subclasses.
    '''

    def update(self, i_game_entity, world, dt):
        raise NotImplementedError()
