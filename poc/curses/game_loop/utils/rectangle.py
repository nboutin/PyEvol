'''
Created on Jul 18, 2019

@author: tbmnxvmuser
'''


class Rectangle():
    """
    Top-Left corner is (0,0)
    """

    def __init__(self, x, y, w, h):
        self._x = x
        self._y = y
        self._w = w
        self._h = h

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def pos(self):
        return (self.x, self.y)

    @property
    def width(self):
        return self._w

    @property
    def height(self):
        return self._h

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self._w

    @property
    def top(self):
        self.x

    @property
    def bottom(self):
        self.x + self._h
