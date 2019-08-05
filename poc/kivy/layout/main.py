import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.splitter import Splitter
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import (Color, Rectangle)


class Background(Widget):
    def __init__(self, **k):
        super().__init__(**k)

        with self.canvas:
            Color(.7, .7, .2)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.redraw, size=self.redraw)

    def redraw(self, instance, pos):
        '''
        When widget position or size change, update rectangle
        '''
        self.rect.pos = self.pos
        self.rect.size = self.size


class MyApp(App):

    def build(self):
        root = FloatLayout()

        root.add_widget(Background(), 2)

        bl = BoxLayout(pos_hint={'center_x': .5, 'top': .99},
                       size=(160, 30), size_hint=(None, None))
        bl.add_widget(Button(text="Play"))
        bl.add_widget(Button(text="Pause"))
        bl.add_widget(Button(text="Step"))
        root.add_widget(bl, 0)

        splitter = Splitter(sizable_from='left', min_size=0,
                            strip_size='6pt', size_hint=(.2, 1), pos_hint={'right': 1})
        splitter.add_widget(Button(text="Label in Splitter"))

        root.add_widget(splitter, 1)

        return root


if __name__ == '__main__':
    MyApp().run()
