'''
Created on 17 juil. 2019

@author: nboutin
'''

import weakref


class GameEntity():

    def __init__(self, controller, physics, render):
        
        self._controller = weakref.ref(controller) if controller else None
        self._physics = weakref.ref(physics) if physics else None
        self._render = weakref.ref(render) if render else None

    @property
    def controller(self):
        return self._controller

    @property
    def physics(self):
        return self._physics

    @property
    def render(self):
        return self._render()
