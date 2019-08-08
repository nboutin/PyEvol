'''
Created on Aug 1, 2019

@author: nboutin
'''
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import (Color, Ellipse, Rectangle)

from evoflatworld.game_system.i_render_strategy import IRenderStrategy
import colors

class CreatureRenderStrategy(IRenderStrategy, Widget):
    def __init__(self, pos, diameter, color, widget_parent):
        '''
        Todo: update widget pos at init ?
        '''
        super().__init__()

        # Parameters
#         radius = diameter / 2

        # Widget
        self.size = (diameter, diameter)
        self._info = None

        with self.canvas:
            Color(*color)
#             x, y = pos
#             self._circle = Ellipse(
#                 pos=(x - radius, y - radius), size=self.size)
            self._circle = Ellipse(pos=pos, size=self.size)
            
            Color(colors.red)
            self._rect_bb = Rectangle()

        self.bind(pos=self._update, size=self._update)

        widget_parent.add_widget(self)

    def _update(self, *args):
        '''Todo: move this to render ?
           use self.pos - radius ?'''
        self._circle.pos = self.pos
        self._circle.size = self.size
        
        if self._info:
            self._info.pos = self.pos
            self._info.text = 'pos:{}\nsize:{}'.format(self.pos, self.size)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if touch.button == 'right':
                if self._info:
                    self.remove_widget(self._info)
                    self._info = None
                else:
                    self._info = Label(font_size='10sp')
                    self.add_widget(self._info)

        return super().on_touch_down(touch)

    def render(self, game_entity, render):
        '''graphics code ...'''
#         self.pos = render.to_parent(*game_entity.pos)
#         print(render.pos)
#         self.pos = (game_entity.pos[0] + render.pos[0], game_entity.pos[1] + render.pos[1])
        self.pos = game_entity.pos
        
        body = game_entity.body
        bb = next(iter(body.shapes)).bb
        
        self._rect_bb.pos = (bb.left, bb.bottom)
        self._rect_bb.size= (bb.right - bb.left, bb.top - bb.bottom) 










