'''
Created on Jul 13, 2019

@author: nboutin
'''

from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse)
from kivy.properties import (NumericProperty, ReferenceListProperty)
from kivy.vector import Vector
from random import uniform

class Ball(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.velocity = Vector(uniform(-5,5), uniform(-5,5))
        d = uniform(10,50)
        self.size = (d,d)
        x,y = kwargs['pos']
        with self.canvas:
            Color(0,0,0,1)
            self.circle = Ellipse(pos=(x-d/2, y-d/2), size=self.size)
        
        self.bind(pos=self._update_circle, size=self._update_circle)
        
    def _update_circle(self, *args):
        self.circle.pos = self.pos
        self.circle.size = self.size
        
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos