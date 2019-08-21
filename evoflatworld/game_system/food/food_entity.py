'''
Created on Aug 11, 2019

@author: nboutin
'''
from evoflatworld.game_system.i_game_entity import IGameEntity


class FoodEntity(IGameEntity):

    def __init__(self, icontroller, iphysics, irender, calories):
        super().__init__(icontroller, iphysics, irender)

        # Parameters
        self.body_shape = None
        self.calories = calories

        # Setup
        iphysics.game_entity(self)
