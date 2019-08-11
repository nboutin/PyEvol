'''
Created on Aug 11, 2019

@author: nboutin
'''
import pymunk


class PhysicsController():

    def __init__(self):

        self._space = pymunk.Space()
        self._space.gravity = (0.0, 0.0)
        self._space.damping = 0.1  # lose 1-x% of its velocity per second

    @property
    def space(self):
        return self._space
