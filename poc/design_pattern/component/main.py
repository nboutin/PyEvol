'''
Created on 17 juil. 2019

@author: nboutin
'''

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from game_system import GameSystem
from functools import partial


class DemoCompApp(App):
    def build(self):

        population = Label(text='0')

        btn_add10 = Button(text='+ 10 rects')
            #,on_press=partial(world.add_balls, 10))

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(btn_add10)
        layout.add_widget(population)

        root = BoxLayout(orientation='vertical')
        self.game_system = GameSystem()
        root.add_widget(self.game_system.widget)
        root.add_widget(layout)

        return root


if __name__ == '__main__':
    DemoCompApp().run()