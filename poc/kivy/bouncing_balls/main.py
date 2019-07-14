'''
Created on Jul 13, 2019

@author: nboutin
'''

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import (Color, Rectangle)
from kivy.vector import Vector
from kivy.properties import (NumericProperty, ReferenceListProperty, ObjectProperty)

from ball import Ball

class BouncingBallsWidget(Widget):
    
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
        b = Ball(pos=touch.pos)
        self.balls.append(b)
        self.add_widget(b)

    def update(self, dt):
        for b in self.balls:
            b.move()
             
            # bounce off top and bottom
            if (b.y < 0) or (b.top > self.height):
                b.velocity_y *= -1
 
            # bounce off left and right
            if (b.x < 0) or (b.right > self.width):
                b.velocity_x *= -1

class BouncingBallsApp(App):
    def build(self):
        w = BouncingBallsWidget()
        Clock.schedule_interval(w.update, 1.0 / 60.0)
        return w
    pass


if __name__ == '__main__':
    BouncingBallsApp().run()
