'''
Created on 17 juil. 2019

@author: nboutin
'''

import weakref


class GameEntity():
    def __init__(self, controller, physics, render):
        self._controller = weakref.ref(controller)
        self._physics = weakref.ref(physics)
        self._render = weakref.ref(render)

#     def update(self, world, graphics):
#         self._input.update(self)
#         self._physics.update(self, world)
#         self._graphics.update(self, graphics)

    @property
    def controller(self):
        return self._controller

    @property
    def physics(self):
        return self._physics

    @property
    def render(self):
        return self._render
