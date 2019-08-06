'''
Created on Aug 5, 2019

@author: nboutin
'''
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton


class TimeControllerWidget(BoxLayout):

    def __init__(self, game_system, **k):
        super().__init__(**k)

        self.game_system = game_system

        self.size = (160, 30)
        self.size_hint = (None, None)

        self._btn_play_pause = ToggleButton(text="Pause")
        btn_step = Button(text="Step")

        self._btn_play_pause.bind(state=self._on_play_pause_state)
        btn_step.bind(on_press=lambda x: self.game_system.step())

        for b in [self._btn_play_pause, btn_step]:
            self.add_widget(b)

    def _on_play_pause_state(self, widget, value):

        print(value)

        if value == 'down':
            self._btn_play_pause.text = 'Play'
            self.game_system.pause()
        elif value == 'normal':
            self._btn_play_pause.text = 'Pause'
            self.game_system.play()
