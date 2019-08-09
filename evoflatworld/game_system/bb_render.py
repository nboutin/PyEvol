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
            self._right = Line()
            self._bottom = Line()

    def __del__(self):
        self._left = None
        self._top = None
        self._right = None
        self._bottom = None

    def render(self, bb):
        self._left.points = [bb.left, bb.bottom, bb.left, bb.top]
        self._top.points = [bb.left, bb.top, bb.right, bb.top]
        self._right.points = [bb.right, bb.top, bb.right, bb.bottom]
        self._bottom.points = [bb.left, bb.bottom, bb.right, bb.bottom]
