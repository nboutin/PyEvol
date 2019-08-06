'''
Created on Aug 6, 2019

@author: nboutin
'''
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock


class FPSMonitorWidget(BoxLayout):

    def __init__(self, **k):
        super().__init__(**k)

        self.size = (30, 15)
        self.size_hint = (None, None)

        self._lb_fps = Label(font_size='10sp')
        self.add_widget(self._lb_fps)

        Clock.schedule_interval(self._update_fps, 1)

    def _update_fps(self, *a):
        self._lb_fps.text = 'FPS : %2.0f\nRFPS: %d' % (
            Clock.get_fps(), Clock.get_rfps())
