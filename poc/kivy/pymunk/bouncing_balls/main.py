'''
Created on Jul 13, 2019

@author: nboutin
'''

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from functools import partial

from world import World


class BouncingBallsApp(App):

    def build(self):
        world = World()

        population = Label(text='0')

        btn_add10 = Button(text='+ 10 rects', on_press=partial(world.add_balls, 10))

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(btn_add10)
        layout.add_widget(population)

        root = BoxLayout(orientation='vertical')
        root.add_widget(world)
        root.add_widget(layout)

        Clock.schedule_interval(world.update, 1.0 / 60.0)
        return root

    pass


if __name__ == '__main__':
    BouncingBallsApp().run()
