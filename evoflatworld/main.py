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
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

from evoflatworld.game_system.game_system import GameSystem
from evoflatworld.time_controller_widget import TimeControllerWidget
from evoflatworld.fps_monitor_widget import FPSMonitorWidget


class EvoFlatWorldApp(App):
    def build(self):
#         Window.maximize()
        Window.set_title("Evo Flat World 0.1.0-alpha")

        root = FloatLayout()

        self.game_system = GameSystem()
        root.add_widget(self.game_system.widget)

#         splitter = Splitter(min_size=0, strip_size='6pt',
# sizable_from='left', rescale_with_parent=True, size_hint=(0.2, 1))

#         info_layout = BoxLayout(orientation='vertical', size_hint=(.2, 1))
#         info_layout.add_widget(Widget()) # blank

        root.add_widget(TimeControllerWidget(self.game_system,
                                             pos_hint={'center_x': .5, 'top': 1}))

        root.add_widget(FPSMonitorWidget(pos_hint={'x': 0.02, 'top': .99}))

        return root


if __name__ == '__main__':
    EvoFlatWorldApp().run()
