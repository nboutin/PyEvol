'''
Created on Aug 2, 2019

@author: nboutin
'''
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Rectangle)

from evoflatworld.game_system.i_render_strategy import IRenderStrategy
import colors

class WorldRenderWidgetStrategy(IRenderStrategy, Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(*colors.black)
            self.__rect = Rectangle(pos=self.pos, size=self.size)

#         self.bind(pos=self._update_rect, size=self._update_rect)

#     def _update_rect(self, instance, pos):
#         self.__rect.pos = self.pos
#         self.__rect.size = self.size

    def render(self, game_entity, render):
        #         self.size = game_entity.size
        pass
