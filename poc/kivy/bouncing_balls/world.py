'''
Created on Jul 14, 2019

@author: nbout
'''

from kivy.uix.widget import Widget
from kivy.graphics import (Color, Rectangle)

from random import random
from ball import Ball

class World(Widget):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.balls = list()
        with self.canvas.before:
            Color(0,1,0,1)
            self.background = Rectangle(size=self.size, pos=self.pos)
            
        # listen to size and position changes
        self.bind(pos=self._update_background, size=self._update_background)
    
    def _update_background(self, instance, value):
        self.background.pos = instance.pos
        self.background.size = instance.size

    def on_touch_down(self, touch):
        self._add_ball(touch.pos)

    def update(self, dt):
        for b in self.balls:
            b.move()
             
            # bounce off top and bottom
            if (b.y < 0) or (b.top > self.height):
                b.velocity_y *= -1
 
            # bounce off left and right
            if (b.x < 0) or (b.right > self.width):
                b.velocity_x *= -1

    def _add_ball(self, pos):
        b = Ball(pos=pos)
        self.balls.append(b)
        self.add_widget(b)
            
    def add_balls(self, n, *largs):
        for x in range(n):
            pos = (random() * self.width + self.x,
                   random() * self.height + self.y)
            self._add_ball(pos)
        
