'''
Created on Jul 13, 2019

@author: nboutin
'''

from kivy.app import App
from kivy.clock import Clock

from world import World

class BouncingBallsApp(App):
    def build(self):
        w = World()
        Clock.schedule_interval(w.update, 1.0 / 60.0)
        return w
    pass


if __name__ == '__main__':
    BouncingBallsApp().run()
