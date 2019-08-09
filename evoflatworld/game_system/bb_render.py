'''
Created on Aug 9, 2019

@author: nboutin
'''
from kivy.graphics import (Color, Line)

import colors


class BBRender():

    def __init__(self, canvas):
        with canvas:
            Color(*colors.Red)
            self._left = Line()
            self._top = Line()

    def render(self, bb):
        self._left.points = [bb.left, bb.bottom, bb.left, bb.top]
        self._top.points = [bb.left, bb.top, bb.right, bb.top]
