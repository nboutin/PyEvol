'''
Created on Aug 11, 2019

@author: nbout
'''
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse)

import colors
from evoflatworld.game_system.i_render_strategy import IRenderStrategy


class FoodRenderStrategy(IRenderStrategy, Widget):

    def __init__(self, pos, diameter, widget_parent, **k):
        super().__init__(**k)

        self.pos = pos
        self.size = (diameter, diameter)

        with self.canvas:
            Color(*colors.Lime)
            self._circle = Ellipse(pos=pos, size=self.size)

        widget_parent.add_widget(self)

    def render(self, game_entity, render):
        self._circle.pos = self.pos
        self._circle.size = self.size
