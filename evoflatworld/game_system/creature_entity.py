'''
Created on Aug 1, 2019

@author: nboutin
'''
from evoflatworld.game_system.i_game_entity import IGameEntity


class CreatureEntity(IGameEntity):
    
    def __init__(self, icontroller, iphysics, irender, pos, diameter):
        super().__init__(icontroller, iphysics, irender)

        self.pos = pos
        self.diameter = diameter
