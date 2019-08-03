'''
Created on Jul 28, 2019

@author: nboutin
'''

# disable Kivy multi-touch emulation
from kivy.config import Config
from pickle import INST
Config.set('input', 'mouse', 'mouse,disable_multitouch,disable_on_activity')

# Can it be move to i_physics_strategy.py ?
# import pymunkoptions
# pymunkoptions.options["debug"] = False

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button

from evoflatworld.game_system.game_system import GameSystem


class EvoFlatWorldApp(App):
    def build(self):
        root = BoxLayout(orientation='horizontal')

        self.game_system = GameSystem()
        root.add_widget(self.game_system.widget)

#         splitter = Splitter(min_size=0, strip_size='6pt',
# sizable_from='left', rescale_with_parent=True, size_hint=(0.2, 1))

        info_layout = BoxLayout(orientation='vertical', size_hint=(.2, 1))

        btn_play = Button(text='Play', size_hint=(1, .1))
        btn_pause = Button(text='Pause', size_hint=(1, .1))
        btn_step = Button(text='Step', size_hint=(1, .1))

        btn_play.bind(on_press=self.play_cbk)
        btn_pause.bind(on_press=self.pause_cbk)
        btn_step.bind(on_press=self.step_cbk)

        info_layout.add_widget(btn_play)
        info_layout.add_widget(btn_pause)
        info_layout.add_widget(btn_step)
        info_layout.add_widget(Widget()) # blank
        root.add_widget(info_layout)

        return root

    def play_cbk(self, instance):
        print("play_cbk:", instance)
        self.game_system.play()

    def pause_cbk(self, instance):
        print("pause_cbk:", instance)
        self.game_system.pause()

    def step_cbk(self, instance):
        print("step_cbk:", instance)
        self.game_system.step()


if __name__ == '__main__':
    EvoFlatWorldApp().run()
