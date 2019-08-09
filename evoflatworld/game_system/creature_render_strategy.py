'''
Created on Aug 1, 2019

@author: nboutin
'''
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import (Color, Ellipse, Rectangle)

import colors
from evoflatworld.game_system.i_render_strategy import IRenderStrategy
from evoflatworld.game_system.bb_render import BBRender


class CreatureRenderStrategy(IRenderStrategy, Widget):

    def __init__(self, pos, diameter, color, widget_parent):
        '''
        Todo: update widget pos at init ?
        '''
        super().__init__()

        # Parameters

        # Widget
        self.size = (diameter, diameter)
        self._info = None
        self._bb_render = None

        with self.canvas:
            Color(*color)
            self._circle = Ellipse(pos=pos, size=self.size)

        self.bind(pos=self._update, size=self._update)

        widget_parent.add_widget(self)

    def _update(self, *args):
        '''Todo: move this to render ?'''
        self._circle.pos = self.pos
        self._circle.size = self.size

        if self._info:
            self._info.pos = self.pos
            self._info.text = 'pos:{}\nsize:{}'.format(self.pos, self.size)

    def game_entity(self, value):
        self._game_entity = value
        
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if touch.button == 'left':
                if self._game_entity._is_selected:
                    self._game_entity._is_selected = False
                    self._bb_render = None
                else:
                    self._game_entity._is_selected = True
                    self._bb_render = BBRender(self.canvas)

            if touch.button == 'right':
                if self._info:
                    self.remove_widget(self._info)
                    self._info = None
                else:
                    self._info = Label(font_size='10sp')
                    self.add_widget(self._info)

        return super().on_touch_down(touch)
    
    def _on_is_selected(self):
        print("on is selected")

    def render(self, game_entity, render):
        '''graphics code ...'''
#         self.pos = render.to_parent(*game_entity.pos)
#         print(render.pos)
#         self.pos = (game_entity.pos[0] + render.pos[0], game_entity.pos[1] + render.pos[1])
#         self.pos = game_entity.pos

        radius = game_entity.diameter / 2
        self.pos = [x - radius for x in game_entity.pos]

        if self._bb_render:
            self._bb_render.render(next(iter(game_entity.body.shapes)).bb)
