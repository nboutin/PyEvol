'''
Created on Jul 13, 2019

@author: nboutin
'''

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock

class BouncingBallsWidget(Widget):
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