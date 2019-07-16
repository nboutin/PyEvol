'''
Created on Jul 14, 2019

@author: nbout
'''

from kivy.uix.widget import Widget
from kivy.graphics import (Color, Rectangle)

import pymunk
import math
from random import (random, uniform, randint)

from ball import Ball


class World(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.balls = list()
        with self.canvas.before:
            Color(0, 1, 0, 1)
            self.background = Rectangle(size=self.size, pos=self.pos)

        # listen to size and position changes
        self.bind(pos=self._update_background, size=self._update_background)

        # Pymunk
        self.space = pymunk.Space()
        self.space.gravity = (0.0, 0.0)
        self.space.damping = 0.1  # lose 1-x% of its velocity per second

    def _update_background(self, instance, value):
        self.background.pos = instance.pos
        self.background.size = instance.size

    def on_touch_down(self, touch):
        self._add_ball(touch.pos)

    def update(self, dt):
        for ball in self.balls:
            ball.move()
        #
        #             _, bottom = self.to_parent(0, 0, True)
        #             _, top = self.to_parent(0, self.height, True)
        #
        #             # bounce off top and bottom
        #             if (ball.y < bottom) or (ball.top > top):
        #                 ball.velocity_y *= -1
        #
        #             # bounce off left and right
        #             if (ball.x < 0) or (ball.right > self.width):
        #                 ball.velocity_x *= -1
        # Pymunk
        self.space.step(dt)

    def _add_ball(self, pos):
        radius = uniform(10, 50)
        angle = math.radians(randint(-180, 180))
        # color

        b = Ball(pos=pos, radius=radius, angle=angle, space=self.space)
        self.balls.append(b)
        self.add_widget(b)

    def add_balls(self, n, *largs):
        for _ in range(n):
            pos = (random() * self.width + self.x,
                   random() * self.height + self.y)
            self._add_ball(pos)
