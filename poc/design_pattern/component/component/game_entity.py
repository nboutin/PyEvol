'''
Created on 17 juil. 2019

@author: nboutin
'''

import weakref


class GameEntity():

    def __init__(self, pos, size, controller, physics, render, **kwargs):

        #         print(pos, size, controller, physics, render, kwargs)

        self.pos = pos
        self.size = size  # for circle, its diameter

#         self._controller = weakref.ref(controller) if controller else None
#         self._physics = weakref.ref(physics) if physics else None
#         self._render = weakref.ref(render) if render else None
        self._controller = controller
        self._physics = physics
        self._render = render

        if self._controller:
            self._controller.build(self)

        if self._physics:
            self._physics.build(self, **kwargs)

        if self._render:
            self._render.build(self, **kwargs)

    @property
    def controller(self):
        return self._controller

    @property
    def physics(self):
        return self._physics

    @property
    def render(self):
        return self._render
