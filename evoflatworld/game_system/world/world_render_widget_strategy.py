'''
Created on Aug 2, 2019

@author: nboutin
'''
from kivy.graphics import (Color, Rectangle)
from kivy.uix.relativelayout import RelativeLayout

from evoflatworld.utils.colors import Colors
from evoflatworld.game_system.i_render_strategy import IRenderStrategy


class WorldRenderWidgetStrategy(IRenderStrategy, RelativeLayout):

    def __init__(self, **k):
        super().__init__(**k)
        
        with self.canvas:
            Color(*Colors.Green2246c)
#            Color(*Colors.Silver)
            self._rect = Rectangle(pos=(0, 0), size=self.size)

    def render(self, game_entity, render):
        pass
