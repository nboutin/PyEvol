'''
Created on Aug 5, 2019

@author: tbmnxvmuser
'''
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class PlayerWidget(BoxLayout):

    def __init__(self, game_system, **k):
        super().__init__(**k)

        self.game_system = game_system

        self.size = (160, 30)
        self.size_hint = (None, None)

        btn_play = Button(text="Play")
        btn_pause = Button(text="Pause")
        btn_step = Button(text="Step")

        btn_play.bind(on_press=lambda x: self.game_system.play())
        btn_pause.bind(on_press=lambda x: self.game_system.pause())
        btn_step.bind(on_press=lambda x: self.game_system.step())

        self.add_widget(btn_play)
        self.add_widget(btn_pause)
        self.add_widget(btn_step)
