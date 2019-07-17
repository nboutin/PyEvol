'''
Created on 17 juil. 2019

@author: nboutin
'''

import weakref


class GameEntity():

    def __init__(self, controller, physics, render):
        if controller:
            self._controller = weakref.ref(controller)
        
        if physics:
            self._physics = weakref.ref(physics)
        
        self._render = weakref.ref(render)

    @property
    def controller(self):
        return self._controller

    @property
    def physics(self):
        return self._physics

    @property
    def render(self):
        return self._render()
