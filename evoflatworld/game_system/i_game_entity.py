'''
Created on Aug 1, 2019

@author: nboutin
'''


class IGameEntity():

    def __init__(self, icontroller, iphysics, irender):
        self._icontroller = icontroller
        self._iphysics = iphysics
        self._irender = irender

    def __del__(self):
        print("del i_game_entity")

    @property
    def controller(self):
        return self._icontroller

    @property
    def physics(self):
        return self._iphysics

    @property
    def render(self):
        return self._irender
