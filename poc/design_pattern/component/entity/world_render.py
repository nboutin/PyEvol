'''
Created on 17 juil. 2019

@author: nboutin
'''

from component.render_comp import RenderComp

from kivy.uix.widget import Widget
from kivy.graphics import (Color, Rectangle)


class WorldRender(RenderComp, Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0, 0, 0, 1)
            self.background = Rectangle(size=self.size, pos=self.pos)

        # listen to size and position changes
        self.bind(pos=self._update_background, size=self._update_background)

    def _update_background(self, instance, _):
        print("update_background")
        self.background.pos = instance.pos
        self.background.size = instance.size

    def render(self, game_entity, render):
        """graphics code ..."""
        pass
