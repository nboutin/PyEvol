'''
Created on Aug 1, 2019

@author: nboutin
'''
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import (Color, Ellipse)

import colors
import evoflatworld.utils.pymunk_util
from evoflatworld.game_system.i_render_strategy import IRenderStrategy
from evoflatworld.game_system.bb_render import BBRender
from evoflatworld.utils.pymunk_util import update_ellipse_from_circle


class CreatureRenderStrategy(IRenderStrategy, Widget):

    def __init__(self, pos, radius, color, widget_parent, **k):

        super().__init__(**k)

        # Parameters

        # Widget
        self.pos = [x - radius for x in pos]
        self.size = [radius * 2, radius * 2]
        self._info = None
        self._bb_render = None

        with self.canvas:
            # Body
            Color(*color)
            self._circle = Ellipse(pos=self.pos, size=self.size)

            # Eyes
            Color(*colors.Black)
            self._eye_left_circle = Ellipse(pos=pos, size=(10, 10))
            self._eye_right_circle = Ellipse(pos=pos, size=(10, 10))

        self.bind(pos=self._update, size=self._update)

        widget_parent.add_widget(self)

    def _update(self, *args):
        if self._info:
            self._info.pos = self.pos
            self._info.text = 'pos:{}\nsize:{}\npowers:{}\nfoods:{}'.format(
                ['{:0.0f}'.format(i) for i in self.pos],
                self.size,
                ["{0:0.2f}".format(i) for i in self._game_entity.powers],
                self._game_entity.energy)

    def game_entity(self, value):
        self._game_entity = value

    def on_touch_down(self, touch):
        try:
            if self.collide_point(*touch.pos):
                if touch.button:
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
                            self._info = Label(font_size='10sp', color=colors.Black)
                            self.add_widget(self._info)
        except AttributeError as e:
            print(e)
                
        return super().on_touch_down(touch)

    def render(self, game_entity, render):
        '''graphics code ...'''
#         self.pos = render.to_parent(*game_entity.pos)

        update_ellipse_from_circle(self._circle, game_entity.body_shape)
        self.pos = self._circle.pos

        # Render eyes
        update_ellipse_from_circle(
            self._eye_left_circle, game_entity.eye_left_shape)
        update_ellipse_from_circle(
            self._eye_right_circle, game_entity.eye_right_shape)

        # Render Bouncing Box
        if self._bb_render:
            self._bb_render.render(game_entity.body_shape.bb)
