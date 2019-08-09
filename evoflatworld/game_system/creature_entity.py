'''
Created on Aug 1, 2019

@author: nboutin
'''
from evoflatworld.game_system.i_game_entity import IGameEntity
from kivy.event import EventDispatcher


class CreatureEntity(IGameEntity, EventDispatcher):

    def __init__(self, icontroller, iphysics, irender, pos, diameter):
        super().__init__(icontroller, iphysics, irender)

        self.pos = pos
        self.diameter = diameter
        self.powers = [2, 2]
        self._is_selected = False

        irender.game_system = self

    @property
    def body(self):
        return self.physics._body
