'''
Created on Aug 9, 2019

@author: nboutin
'''
from kivy.graphics import (Color, Line)

from evoflatworld.utils.colors import Colors


class BBRender():
    ''' Todo: inherit from Widget to avoid Exception during Window resize'''

    def __init__(self, canvas):
        self._canvas = canvas
        with canvas:
            Color(*Colors.Red)
            self._left = Line()
            self._top = Line()
            self._right = Line()
            self._bottom = Line()

    def __del__(self):
        self._canvas.remove(self._left)
        self._canvas.remove(self._top)
        self._canvas.remove(self._right)
        self._canvas.remove(self._bottom)

    def render(self, bb):
        self._left.points = [bb.left, bb.bottom, bb.left, bb.top]
        self._top.points = [bb.left, bb.top, bb.right, bb.top]
        self._right.points = [bb.right, bb.top, bb.right, bb.bottom]
        self._bottom.points = [bb.left, bb.bottom, bb.right, bb.bottom]
