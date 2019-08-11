'''
Created on Aug 11, 2019

@author: nboutin
'''
from evoflatworld.game_system.i_game_entity import IGameEntity


class FoodEntity(IGameEntity):
    def __init__(self, icontroller, iphysics, irender, pos, diameter):
        super().__init__(icontroller, iphysics, irender)

        # Parameters