'''
Created on Jul 13, 2019

@author: nboutin
'''

from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse)

from ball_physics import BallPhysics


class Ball(Widget):
    def __init__(self, **kwargs):
        """
        :param pos, (x,y) (mandatory)
        :param radius (radians)
        :param color (rgba)
        """
        # Parameters
        pos = kwargs['pos']
        radius = kwargs.get('radius', 10)
        color = kwargs.get('color', (1, 1, 1, 1))
        
        # Widget
        super().__init__()
        self.size = (radius*2, radius*2)

        with self.canvas:
            Color(*color)
            x, y = pos
            self.__circle = Ellipse(
                pos=(x - radius, y - radius), size=self.size)

        self.bind(pos=self._update_circle, size=self._update_circle)

        # Pymunk
        self.__physics = BallPhysics(**kwargs)

    def _update_circle(self, *args):
        self.__circle.pos = self.pos
        self.__circle.size = self.size

    def move(self):
        self.__physics.move()
        self.pos = self.__physics.pos

    def render(self):
        self.pos = self.__physics.pos
