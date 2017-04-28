import pygame

from color import *


class Food:

    COLOR = RED
    SIZE = 20

    def __init__(self, pos):
        self.rect = pygame.rect.Rect((0, 0), (Food.SIZE, Food.SIZE))
        self.rect.center = pos
        self.calories = 20

    def eat(self, q):
        if self.calories - q > 0:
            self.calories -= q
            return q
        else:
            tmp = self.calories
            self.calories = 0
            return tmp

    def render(self, surface):
        pygame.draw.circle(surface, Food.COLOR, self.rect.center, int(Food.SIZE/2))

