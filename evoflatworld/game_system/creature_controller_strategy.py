'''
Created on Aug 8, 2019

@author: nboutin
'''
from evoflatworld.game_system.i_controller import IController
from kivy.core.window import Window
from kivy.uix.widget import Widget


class CreatureControllerStrategy(IController, Widget):

    def __init__(self):
        self._keyboard = Window.request_keyboard(
            self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        print(keyboard, keycode, text, modifiers)

    def update(self, i_game_entity):
        pass
