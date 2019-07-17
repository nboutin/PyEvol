'''
Created on 17 juil. 2019

@author: nboutin
'''

from game_object import GameObject
from general_input import GeneralInput
from ball_physics import BallPhysics
from ball_graphics import BallGraphics


class World():

    def __init__(self):
        self._entities = list()

        for _ in range(5):
            self._entities.append(self.createBall())

    def game_loop(self):
        while True:
            for e in self._entities:
                e.update(self, graphics)

    def createBall(self):
        return GameObject(GeneralInput(), BallPhysics(), BallGraphics())


if __name__ == '__main__':
    w = World()
    w.game_loop()
