'''
Created on Aug 1, 2019

@author: nboutin
'''
from evoflatworld.game_system.i_game_entity import IGameEntity


class CreatureEntity(IGameEntity):

    def __init__(self, icontroller, iphysics, irender, pos, diameter):
        super().__init__(icontroller, iphysics, irender)

        # Parameters
        self.pos = pos
        self.diameter = diameter
        self.powers = [2, 2]
        self._is_selected = False

        # Setup
        icontroller.game_entity(self)
        irender.game_entity(self)

    @property
    def body(self):
        return self.physics._body
