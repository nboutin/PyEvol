'''
Created on Aug 8, 2019

@author: nboutin
'''
from evoflatworld.game_system.i_controller_strategy import IControllerStrategy
from kivy.core.window import Window
from kivy.uix.widget import Widget


class CreatureControllerStrategy(IControllerStrategy, Widget):

    def __init__(self, **k):
        super().__init__(**k)
        self._keyboard = None

    def game_entity(self, value):
        self._game_entity = value

    def _request_keyboard(self):
        self._keyboard = Window.request_keyboard(
            self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)

    def _on_keyboard_closed(self):
        if self._keyboard:
            self._keyboard.unbind(on_key_down=self._on_key_down)
            self._keyboard = None

        # Keyboard requested elsewhere, so creature not selected anymore
        self._game_entity._is_selected = False

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        '''Todo: launch timer that decrease power step by step'''

        key = keycode[1]
        turn = 0.5
        speed = 0.5

        if key == 'right':
            self._game_entity.powers[0] -= turn
            self._game_entity.powers[1] += turn
        if key == 'left':
            self._game_entity.powers[0] += turn
            self._game_entity.powers[1] -= turn
        if key == 'up':
            self._game_entity.powers[0] += speed
            self._game_entity.powers[1] += speed
        if key == 'down':
            self._game_entity.powers[0] -= speed
            self._game_entity.powers[1] -= speed

        # Accept the key otherwise it will be used by the system
        return True

    def update(self, game_entity):

        if not self._keyboard and game_entity._is_selected:
            self._request_keyboard()

        # Do not release keyboard manually, it will be release when something else
        # request it
