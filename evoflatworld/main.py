'''
Created on Jul 28, 2019

@author: nboutin
'''

# disable Kivy multi-touch emulation
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch,disable_on_activity')

# Can it be move to i_physics_strategy.py ?
# import pymunkoptions
# pymunkoptions.options["debug"] = False

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.splitter import Splitter

from kivy.uix.button import Button
from evoflatworld.game_system.game_system import GameSystem


class EvoFlatWorldApp(App):
    def build(self):
        root = BoxLayout(orientation='horizontal')

        self.game_system = GameSystem()
        root.add_widget(self.game_system.widget)

#         splitter = Splitter(min_size=0, strip_size='6pt',
#                             sizable_from='left', rescale_with_parent=True, size_hint=(0.2, 1))
#         info = Widget(size_hint=(0.2, 1))
        info_layout = BoxLayout(size_hint=(.2, 1))

        btn = Button(text='button')

        info_layout.add_widget(btn)
#         splitter.add_widget(btn)

        root.add_widget(info_layout)

        return root


if __name__ == '__main__':
    EvoFlatWorldApp().run()
