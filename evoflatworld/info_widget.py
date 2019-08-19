'''
Created on Aug 18, 2019

@author: nboutin
'''
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import (Color, Rectangle)

import colors


class InfoWidget(BoxLayout):

    def __init__(self, **k):
        super().__init__(**k)

        self.size = (350, 600)
        self.size_hint = (None, None)
        self.orientation = 'vertical'

        self.add_widget(Widget())

        with self.canvas.before:
            Color(*colors.Gray)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    def add_entity(self, entity):
        self.add_creature(entity)

    def add_creature(self, creature):
        '''
        Todo: check for already added creature
        '''
        label = Label(size_hint=(1, .2))
        label.text = 'pos:{}\nsize:{}\npowers:{}\nfoods:{}'.format(
            ['{:0.0f}'.format(i) for i in creature.render.pos],
            creature.render.size,
            ["{0:0.2f}".format(i) for i in creature.powers],
            creature.energy)
        self.add_widget(label)
