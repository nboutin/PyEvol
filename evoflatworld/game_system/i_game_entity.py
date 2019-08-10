'''
Created on Aug 1, 2019

@author: nboutin
'''


class IGameEntity():

    def __init__(self, icontroller, iphysics, irender):
        self._icontroller = icontroller
        self._iphysics = iphysics
        self._irender = irender

    @property
    def controller(self):
        return self._icontroller

    @property
    def physics(self):
        return self._iphysics

    @property
    def render(self):
        return self._irender
