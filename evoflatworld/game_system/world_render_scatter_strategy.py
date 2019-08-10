'''
Created on Aug 1, 2019

@author: nboutin
'''

from kivy.uix.scatter import Scatter
from kivy.graphics import (Color, Rectangle)
from kivy.graphics.transformation import Matrix

from evoflatworld.game_system.i_render_strategy import IRenderStrategy
from kivy.uix.scatterlayout import ScatterLayout


class WorldRenderScatterStrategy(IRenderStrategy, Scatter):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

#         self.size_hint = (None, None)   # Why ?
        self.do_rotation = False
        self.scale_min = 1
        self.scale_max = 10

        # canvas.after mandatory ?
        with self.canvas:
            Color(0, 1, 0, 1)
            self._rect = Rectangle(pos=self.pos, size=self.bbox[1])

        self.bind(pos=self._update_rect, size=self._update_rect)

    def _update_rect(self, instance, pos):
        '''
        Bounding box of the widget in parent space:
        ((x, y), (w, h))
        x, y = lower left corner
        '''
        #         self._rect.pos = self.pos
#         print(pos, self.pos, self._rect.pos)
#         print(self.bbox)
        self._rect.pos = self.bbox[0]
        self._rect.size = self.bbox[1]

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            if touch.is_mouse_scrolling:
                if touch.button == 'scrolldown':
                    mat = Matrix().scale(.9, .9, .9)
                    self.apply_transform(mat, anchor=touch.pos)
                elif touch.button == 'scrollup':
                    mat = Matrix().scale(1.1, 1.1, 1.1)
                    self.apply_transform(mat, anchor=touch.pos)
        return super().on_touch_up(touch)

    def render(self, game_entity, render):
#         self.size = game_entity.size
        pass
