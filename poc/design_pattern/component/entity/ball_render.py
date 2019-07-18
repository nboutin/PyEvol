'''
Created on 17 juil. 2019

@author: nboutin
'''

from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse)

from component.render_comp import RenderComp


class BallRender(RenderComp, Widget):
    """
    TODO can it be only a Canvas ?
    """

    def __init__(self, **kwargs):
        # Parameters
        widget = kwargs['widget']
        pos = kwargs['pos']
        radius = kwargs.get('radius', 10)
        color = kwargs.get('color', (1, 1, 1, 1))

        super().__init__()
        self.size = (radius * 2, radius * 2)
#         size = (radius * 2, radius * 2)

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
        pass
