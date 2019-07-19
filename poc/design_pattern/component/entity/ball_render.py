'''
Created on 17 juil. 2019

@author: nboutin
'''

from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse)

from component.render_comp import RenderComp


class BallRender(RenderComp, Widget):
    """
    Todo: can it be only a Canvas ?
    """
    def __init__(self):
        super().__init__()

    def build(self, game_entity, **kwargs):
        """
        :param game_entity
            :param pos
            :param size
        :param widget (mandatory)
        
        Todo: update widget pos at init ?
        """
        # Parameters
        pos = game_entity.pos
        widget = kwargs['widget']
        radius = game_entity.size / 2
        color = kwargs.get('color', (.2, .2, .2, 1))

        # Widget
        # self.size = (radius * 2, radius * 2)
        self.size = (game_entity.size, game_entity.size)

        with self.canvas:
            Color(*color)
            x, y = pos
            self.__circle = Ellipse(
                pos=(x - radius, y - radius), size=self.size)

        self.bind(pos=self._update_circle, size=self._update_circle)
        
        widget.add_widget(self)


    def _update_circle(self, *args):
        # TODO move this to render ?
        self.__circle.pos = self.pos
        self.__circle.size = self.size    


    def render(self, game_entity, render):
        """graphics code ..."""
        self.pos = game_entity.pos

