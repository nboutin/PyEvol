'''
Created on Jul 13, 2019

@author: nboutin
'''

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse

class BouncingBallsWidget(Widget):
    
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 1, 0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
    
    def update(self, dt):
        pass

class BouncingBallsApp(App):
    def build(self):
        w = BouncingBallsWidget()
        Clock.schedule_interval(w.update, 1.0 / 60.0)
        return w
    pass


if __name__ == '__main__':
    BouncingBallsApp().run()
