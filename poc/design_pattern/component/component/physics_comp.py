'''
Created on 17 juil. 2019

@author: nboutin
'''


class PhysicsComp():

    def build(self, game_entity, **kwargs):
        raise NotImplementedError()

    def update(self, game_entity, world, dt):
        raise NotImplementedError()
