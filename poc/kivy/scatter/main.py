'''
Created on Jul 19, 2019

@author: nboutin
'''


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.graphics import (Color, Rectangle)
from kivy.graphics.transformation import Matrix


class World(Scatter):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.scale_min=.1
        self.scale_max = 10

        with self.canvas:
            Color(0.4, 0.4, 0.4, 1)
            self.background = Rectangle(size=self.size, pos=self.pos)

        self.bind(pos=self._update_background, size=self._update_background)

    def _update_background(self, instance, _):
        self.background.pos = instance.pos
        self.background.size = instance.size
        
    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            if touch.button == 'scrolldown':
                print ("scrolldown")
            elif touch.button == 'scrollup':
                print("scrollup")
        
#         mat = Matrix().scale(.3,.3,.3)
#         self.apply_transform(mat)

class ScatterApp(App):

    def build(self):
        return World()


if __name__ == '__main__':
    ScatterApp().run()
