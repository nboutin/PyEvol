'''
Created on Aug 1, 2019

@author: nboutin
'''
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import (Color, Ellipse)

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
            # Body
            Color(*color)
            self._circle = Ellipse(pos=pos, size=self.size)

            # Eyes
            Color(*colors.Black)
            self._eye_left_circle = Ellipse(pos=pos, size=(10, 10))
            self._eye_right_circle = Ellipse(pos=pos, size=(10, 10))

        self.bind(pos=self._update, size=self._update)

        widget_parent.add_widget(self)

    def _update(self, *args):
        '''
        Todo: move this to render ?
        Is it usefull ?
        '''
#         self._circle.pos = self.pos
#         self._circle.size = self.size

        if self._info:
            self._info.pos = self.pos
            self._info.text = 'pos:{}\nsize:{}\npowers:{}'.format(
                ['{:0.0f}'.format(i) for i in self.pos], 
                self.size, 
                ["{0:0.2f}".format(i) for i in self._game_entity.powers])

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

    def render(self, game_entity, render):
        '''graphics code ...'''
#         self.pos = render.to_parent(*game_entity.pos)
#         print(render.pos)
#         self.pos = (game_entity.pos[0] + render.pos[0], game_entity.pos[1] + render.pos[1])
#         self.pos = game_entity.pos

        # Render physical position of body on widget
#         radius = game_entity.diameter / 2
#         self.pos = [x - radius for x in game_entity.pos]
#         print(game_entity.body_bb)
        self.pos = (game_entity.body_bb.left, game_entity.body_bb.bottom)

        self._circle.pos = self.pos
        self._circle.size = self.size

        # Render eyes
        # Todo: use bb size
        self._eye_left_circle.pos = (game_entity.eye_left_bb.left,
                                     game_entity.eye_left_bb.bottom)
        self._eye_left_circle.size = (3, 3)
        self._eye_right_circle.pos = (game_entity.eye_right_bb.left,
                                      game_entity.eye_right_bb.bottom)
        self._eye_right_circle.size = (3, 3)

        # Render Bouncing Box
        if self._bb_render:
            self._bb_render.render(game_entity.body_bb)
