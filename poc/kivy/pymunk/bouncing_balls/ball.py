'''
Created on Jul 13, 2019

@author: nboutin
'''

from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse)
from kivy.properties import (NumericProperty, ReferenceListProperty)
from kivy.vector import Vector
from random import uniform
import pymunk
import math
import random

class Ball(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def __init__(self, pos, space, **kwargs):
        super().__init__(**kwargs)
        self.velocity = Vector(uniform(-5,5), uniform(-5,5))
        d = uniform(10,50)
        self.size = (d,d)
        x,y = pos
        with self.canvas:
            Color(0,0,0,1)
            self.circle = Ellipse(pos=(x-d/2, y-d/2), size=self.size)
        
        self.bind(pos=self._update_circle, size=self._update_circle)
        
        # Pymunk
        self.space = space
        self.mass = 4
        self.radius = d/2
        self.force = 180
        angle = math.radians(random.randint(-180, 180))
        
        moment = pymunk.moment_for_circle(self.mass, 0, self.radius)

        self.body = pymunk.Body(self.mass, moment)
        self.body.position = self.circle.pos
        self.body.angle = angle

        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.elasticity = 0.95
        self.shape.friction = 0.9
#         self.shape.collision_type = constants.collision_types['creature']
#         self.shape.filter = pymunk.ShapeFilter(categories=constants.categories['creature'])

        self.space.add(self.body, self.shape)

        
    def _update_circle(self, *args):
        self.circle.pos = self.pos
        self.circle.size = self.size
        
    def move(self):
#         pass
#         self.pos = Vector(*self.velocity) + self.pos
        powers = [5,5]
        p1 = powers[0] * self.force
        p2 = powers[1] * self.force
        self.body.apply_force_at_local_point((p1, 0), (0, -self.radius))
        self.body.apply_force_at_local_point((p2, 0), (0, +self.radius))

#         print (self.body.position)
        self.pos = self.body.position.int_tuple
