'''
Created on 17 juil. 2019

@author: nboutin
'''

import weakref


class GameObject():
    def __init__(self, input_comp, physics, graphics):
        self._pos = (0, 0)
        self._input = weakref.ref(input_comp)
        self._physics = weakref.ref(physics)
        self._graphics = weakref.ref(graphics)

    def update(self, world, graphics):
        self._input.update(self)
        self._physics.update(self, world)
        self._graphics.update(self, graphics)
