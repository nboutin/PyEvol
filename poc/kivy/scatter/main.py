'''
Created on Jul 19, 2019

@author: nboutin
'''

# disable multi-touch emulation
from kivy.config import Config
# Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
# Config.set('input', 'mouse', 'mouse,disable_multitouch')
# Config.set('input', 'mouse', 'disable_on_activity')
Config.set('input', 'mouse', 'mouse,disable_multitouch,disable_on_activity')

from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.graphics import (Color, Rectangle)
from kivy.graphics.transformation import Matrix


class World(Scatter):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.do_rotation = False
        self.scale_min = .1
        self.scale_max = 10
        self.top = 500

        with self.canvas.after:
            Color(0, 1, 0)
            self.rect = Rectangle(pos=self.pos, size=self.bbox[1])

        self.bind(pos=self._update_rect, size=self._update_rect)

    def _update_rect(self, instance, _):
        self.rect.pos = self.pos
        self.rect.size = self.bbox[1]

#     def on_transform_with_touch(self, touch):
#         print("on_transform_with_touch:", touch)

    def on_touch_move(self, touch):
        print("on_touch_move:", touch.profile, touch)
        return super().on_touch_move(touch)

    def on_touch_down(self, touch):
        print("on_touch_down:", touch.profile, touch)
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            print("on_touch_up:", touch.profile, touch)

            if touch.is_mouse_scrolling:
                print ("is_mouse_scrolling")
                if touch.button == 'scrolldown':
                    print("scrolldown")
                    mat = Matrix().scale(.9, .9, .9)
                    self.apply_transform(mat, anchor=touch.pos)
#                     return True
                elif touch.button == 'scrollup':
                    print("scrollup")
                    mat = Matrix().scale(1.1, 1.1, 1.1)
                    self.apply_transform(mat, anchor=touch.pos)
#                     return True
        
        return super().on_touch_up(touch)

class ScatterApp(App):
    def build(self):
        return World(size=(400, 400), size_hint=(None, None))


if __name__ == '__main__':
    ScatterApp().run()
