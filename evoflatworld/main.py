'''
Created on Jul 28, 2019

@author: nboutin
'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.splitter import Splitter

from kivy.uix.widget import Widget
from kivy.graphics import (Color, Rectangle)
from kivy.uix.button import Button


class World(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Color(1, 1, 0)
            self.background = Rectangle(size=self.size, pos=self.pos)

        # listen to size and position changes
        self.bind(pos=self._update_background, size=self._update_background)

    def _update_background(self, instance, _):
        self.background.pos = instance.pos
        self.background.size = instance.size


class EvoFlatWorldApp(App):
    def build(self):
        root = BoxLayout()

        world = World()
        root.add_widget(world)

        splitter = Splitter(min_size=0, strip_size='4pt',
                            sizable_from='left', rescale_with_parent=True, size_hint=(0.2, 1))

        btn = Button(text='button')
        splitter.add_widget(btn)

        root.add_widget(splitter)

        return root


if __name__ == '__main__':
    EvoFlatWorldApp().run()
