'''
Created on Jul 28, 2019

@author: nboutin
'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.splitter import Splitter

from kivy.uix.button import Button
from evoflatworld.game_system.game_system import GameSystem


class EvoFlatWorldApp(App):
    def build(self):
        root = BoxLayout()

        self.game_system = GameSystem()
        root.add_widget(self.game_system.widget)

        splitter = Splitter(min_size=0, strip_size='6pt',
                            sizable_from='left', rescale_with_parent=True, size_hint=(0.2, 1))

        btn = Button(text='button')
        splitter.add_widget(btn)

        root.add_widget(splitter)

        return root


if __name__ == '__main__':
    EvoFlatWorldApp().run()
