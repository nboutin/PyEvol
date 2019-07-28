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

        self.scale_min = .1
        self.scale_max = 10
        self.top = 500

        with self.canvas:
            Color(0, 1, .5, mode='hsv')
            self.rectA = Rectangle(size=self.size)

        self.bind(size=self._update_rectA)
        
        with self.canvas.after:
            Color(.1, 1, .5, .2, mode='hsv')
            self.rectB = Rectangle(pos=self.pos, size=self.bbox[1])
            
        self.bind(pos=self._update_rectB, size=self._update_rectB)

    def _update_rectA(self, instance, _):
        self.rectA.size = self.size

    def _update_rectB(self, instance, _):
        self.rectB.pos = self.pos
        self.rectB.size = self.bbox[1]

    def on_touch_move(self, touch):
        print ("on_touch_move:", touch)
        self.center = touch.pos
        
    def on_touch_down(self, touch):
        pass
#         if touch.is_mouse_scrolling:
#             if touch.button == 'scrolldown':
#                 print("scrolldown")
#                 print(self.transform)
#                 mat = Matrix().scale(.9, .9, .9)
#                 self.apply_transform(mat)
#                 print(self.transform)
#                 print(self.pos)
#                 print(self.rect.pos)
#                 print(self.to_local(1, 1, relative=True))
#                 print(self.to_widget(1, 1, relative=True))
#                 print(self.to_parent(1, 1, relative=True))
#                 self.rect.pos = self.to_local()
#             elif touch.button == 'scrollup':
#                 print("scrollup")
#                 print(self.transform)
#                 mat = Matrix().scale(1.1, 1.1, 1.1)
#                 self.apply_transform(mat)

#     def on_transform_with_touch(self, touch):
#         print("on_transform_with_touch")


class ScatterApp(App):
    def build(self):
        return World(size=(400, 400), size_hint=(None, None))


if __name__ == '__main__':
    ScatterApp().run()
