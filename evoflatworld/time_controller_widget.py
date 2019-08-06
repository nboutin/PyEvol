'''
Created on Aug 5, 2019

@author: nboutin
'''
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton


class TimeControllerWidget(BoxLayout):

    def __init__(self, game_system, **k):
        super().__init__(**k)

        self.game_system = game_system

        self.size = (180, 30)
        self.size_hint = (None, None)

        self._btn_play_pause = ToggleButton(text="Pause")
        btn_step = Button(text="Step")
        btn_speed_down = Button(text='-', size_hint=(.5, 1))
        btn_speed_up = Button(text='+', size_hint=(.5, 1))
        self._lb_speed = Label(
            size_hint=(.5, 1), text='{}'.format(self.game_system.speed))

        self._btn_play_pause.bind(state=self._on_play_pause_state)
        btn_step.bind(on_press=lambda x: self.game_system.step())
        btn_speed_down.bind(on_press=self._on_speed_down)
        btn_speed_up.bind(on_press=self._on_speed_up)

        for b in [btn_speed_down, self._btn_play_pause, btn_step, btn_speed_up, self._lb_speed]:
            self.add_widget(b)

    def _on_speed_down(self, _):
        self.game_system.speed_down()
        self._lb_speed.text = '{}'.format(self.game_system.speed)

    def _on_speed_up(self, _):
        self.game_system.speed_up()
        self._lb_speed.text = '{}'.format(self.game_system.speed)

    def _on_play_pause_state(self, widget, value):

        if value == 'down':
            self._btn_play_pause.text = 'Play'
            self.game_system.pause()
        elif value == 'normal':
            self._btn_play_pause.text = 'Pause'
            self.game_system.play()
