'''
Created on Aug 1, 2019

@author: nboutin
'''
from evoflatworld.game_system.i_game_entity import IGameEntity


class CreatureEntity(IGameEntity):

    def __init__(self, icontroller, iphysics, irender):
        super().__init__(icontroller, iphysics, irender)

        # Parameters
        self.body_shape = None
        self.eye_left_shape = None
        self.eye_right_shape = None

        self.energy = 0    # Food
        self.powers = [2, 2]
        self._is_selected = False

        # Setup
        icontroller.game_entity(self)
        iphysics.game_entity(self)
        irender.game_entity(self)
