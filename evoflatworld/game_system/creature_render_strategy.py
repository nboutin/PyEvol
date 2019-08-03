'''
Created on Aug 1, 2019

@author: nboutin
'''
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse)

from evoflatworld.game_system.i_render_strategy import IRenderStrategy


class CreatureRenderStrategy(IRenderStrategy, Widget):
    def __init__(self, pos, diameter, widget_parent):
        '''
        Todo: update widget pos at init ?
        '''
        super().__init__()

        # Parameters
        radius = diameter / 2
        red = (1, 0, 0)

        # Widget
        self.size = (diameter, diameter)

        with self.canvas:
            Color(*red)
            x, y = pos
            self.__circle = Ellipse(
                pos=(x - radius, y - radius), size=self.size)

        self.bind(pos=self._update_circle, size=self._update_circle)

        widget_parent.add_widget(self)

    def _update_circle(self, *args):
        '''
        Todo: move this to render ?
        '''
        self.__circle.pos = self.pos
        self.__circle.size = self.size

    def render(self, game_entity, render):
        '''graphics code ...'''
#         self.pos = render.to_parent(*game_entity.pos)
        self.pos = game_entity.pos
#         print(render.pos)
#         self.pos = (game_entity.pos[0] + render.pos[0], game_entity.pos[1] + render.pos[1]) 
