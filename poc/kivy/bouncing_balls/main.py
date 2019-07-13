'''
Created on Jul 13, 2019

@author: nboutin
'''

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.vector import Vector

class BouncingBallsWidget(Widget):
    
    def __init__(self, **kwargs):
        Widget.__init__(self, **kwargs)
        self.balls = list()
    
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 1, 0)
            d = 30.
            b = Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            self.balls.append(b)
    
    def update(self, dt):
        for b in self.balls:
            b.pos = Vector(4,0) + b.pos

class BouncingBallsApp(App):
    def build(self):
        w = BouncingBallsWidget()
        Clock.schedule_interval(w.update, 1.0 / 60.0)
        return w
    pass


if __name__ == '__main__':
    BouncingBallsApp().run()
