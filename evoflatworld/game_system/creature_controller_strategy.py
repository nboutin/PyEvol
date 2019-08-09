'''
Created on Aug 8, 2019

@author: nboutin
'''
from evoflatworld.game_system.i_controller_strategy import IControllerStrategy
from kivy.core.window import Window
from kivy.event import EventDispatcher


class CreatureControllerStrategy(IControllerStrategy, EventDispatcher):

    def __init__(self, **k):
        super().__init__(**k)
        self._keyboard = None

    def game_entity(self, value):
        self._game_entity = value

    def _request_keyboard(self):
        print("request keyboard")
        self._keyboard = Window.request_keyboard(
            self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)

    def _on_keyboard_closed(self):
        print("_on_keyboard_closed")
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

        # Keyboard requested elsewhere, so creature not selected anymore
        self._game_entity._is_selected = False

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        '''Todo: launch timer that decrease power step by step'''
        
        key = keycode[1]
        if key =='right':
            self._game_entity.powers[1] += 1
        if key =='left':
            self._game_entity.powers[0] += 1
        if key =='up':
            self._game_entity.powers[0] += 1
            self._game_entity.powers[1] += 1
        if key =='down':
            self._game_entity.powers[0] -= 1
            self._game_entity.powers[1] -= 1

        # Accept the key otherwise it will be used by the system
        return True

    def update(self, game_entity):

        if not self._keyboard and game_entity._is_selected:
            self._request_keyboard()
        elif self._keyboard and not game_entity._is_selected:
            self._on_keyboard_closed()
