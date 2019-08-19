'''
Created on Jul 28, 2019

@author: nboutin
'''

# disable Kivy multi-touch emulation
from kivy.config import Config
from evoflatworld import time_controller_widget
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
from evoflatworld.info_widget import InfoWidget


class RootLayout(FloatLayout):

    def __init__(self, game_system, info_widget, **k):
        super().__init__(**k)

        self.game_system = game_system
        self.info_widget = info_widget

    def on_touch_down(self, touch):
        for e in self.game_system._entities:
            pos = e.render.to_widget(*touch.pos)
            if e.render.collide_point(*pos):
                self.info_widget.add_entity(e)

        return super().on_touch_down(touch)


class EvoFlatWorldApp(App):
    def build(self):
        Window.maximize()
        self.title = "Evo Flat World 0.2.0-dev"

        self._game_system = GameSystem()
        info_widget = InfoWidget(pos_hint={'right': .99, 'center_y': .5})
        time_controller_widget = TimeControllerWidget(self._game_system,
                                                      pos_hint={'center_x': .5, 'top': 1})
        fps_monitor_widget = FPSMonitorWidget(pos_hint={'x': 0.02, 'top': .99})

        root = RootLayout(self._game_system, info_widget)

        root.add_widget(self._game_system.widget)
        root.add_widget(time_controller_widget)
        root.add_widget(fps_monitor_widget)
        root.add_widget(info_widget)

        return root


if __name__ == '__main__':
    EvoFlatWorldApp().run()
