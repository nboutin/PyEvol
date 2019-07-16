'''
Created on Jul 13, 2019

@author: nboutin
'''

from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse)
from kivy.properties import (NumericProperty, ReferenceListProperty)
from kivy.vector import Vector

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
        color = kwargs.get('color', (0, 0, 0, 1))

        # Widget
        super().__init__(**kwargs)
        self.size = (radius, radius)

        with self.canvas:
            Color(color)
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
        # powers = [10, 10]
        # p1 = powers[0] * self.force
        # p2 = powers[1] * self.force
        # self.__body.apply_force_at_local_point((p1, 0), (0, -self.radius))
        # self.__body.apply_force_at_local_point((p2, 0), (0, +self.radius))

        # Update Widget position
        #         self.pos = self.__body.position.int_tuple
        #         self.pos = self.__physics.pos
        self.pos = self.__physics.move()
