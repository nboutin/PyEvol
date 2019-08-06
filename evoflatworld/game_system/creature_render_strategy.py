'''
Created on Aug 1, 2019

@author: nboutin
'''
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import (Color, Ellipse)

from evoflatworld.game_system.i_render_strategy import IRenderStrategy


class CreatureRenderStrategy(IRenderStrategy, Widget):
    def __init__(self, pos, diameter, color, widget_parent):
        '''
        Todo: update widget pos at init ?
        '''
        super().__init__()

        # Parameters
        radius = diameter / 2

        # Widget
        self.size = (diameter, diameter)

        with self.canvas:
            Color(*color)
            x, y = pos
            self.__circle = Ellipse(
                pos=(x - radius, y - radius), size=self.size)

        self.bind(pos=self._update, size=self._update)

        self._info = Label(font_size='10sp')
        self.add_widget(self._info)

        widget_parent.add_widget(self)

    def _update(self, *args):
        '''Todo: move this to render ?
           use self.pos - radius ?'''
        self.__circle.pos = self.pos
        self.__circle.size = self.size
        self._info.pos = self.pos
        self._info.text = 'pos:{}\nsize:{}'.format(self.pos, self.size)

    def render(self, game_entity, render):
        '''graphics code ...'''
#         self.pos = render.to_parent(*game_entity.pos)
        self.pos = game_entity.pos
#         print(render.pos)
#         self.pos = (game_entity.pos[0] + render.pos[0], game_entity.pos[1] + render.pos[1])
