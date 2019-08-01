'''
Created on Aug 1, 2019

@author: nboutin
'''

from kivy.uix.widget import Widget
from kivy.graphics import (Color, Rectangle)

from evoflatworld.game_system.i_render_strategy import IRenderStrategy


class WorldRenderStrategy(IRenderStrategy, Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Color(0, 1, 0, 1)
            self.background = Rectangle(size=self.size, pos=self.pos)

        # listen to size and position changes
        #self.bind(pos=self._update_background, size=self._update_background)
        self.bind(pos=self._update_background)

    def _update_background(self, instance, _):
        self.background.pos = instance.pos
#         self.background.size = instance.size

    def render(self, game_entity, render):
        pass
