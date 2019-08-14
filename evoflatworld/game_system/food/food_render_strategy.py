'''
Created on Aug 11, 2019

@author: nboutin
'''
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse)

import colors
from evoflatworld.game_system.i_render_strategy import IRenderStrategy
from evoflatworld.utils.pymunk_util import update_ellipse_from_circle


class FoodRenderStrategy(IRenderStrategy, Widget):

    def __init__(self, pos, radius, widget_parent, **k):
        super().__init__(**k)

        # Widget
        self.pos = [x - radius for x in pos]
        self.size = [radius * 2, radius * 2]

        with self.canvas:
            Color(*colors.Lime)
            self._circle = Ellipse(pos=self.pos, size=self.size)

        widget_parent.add_widget(self)

    def render(self, game_entity, render):
        update_ellipse_from_circle(self._circle, game_entity.body_shape)
