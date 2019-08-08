'''
Created on Aug 2, 2019

@author: nboutin
'''
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Rectangle)

from evoflatworld.game_system.i_render_strategy import IRenderStrategy
import colors


class WorldRenderWidgetStrategy(IRenderStrategy, Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(*colors.green)
            self._rect = Rectangle(pos=self.pos, size=self.size)

    def render(self, game_entity, render):
        pass
