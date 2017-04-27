import pygame

from color import *


class Food:

    COLOR = RED
    SIZE = 20

    def __init__(self, pos):
        self.rect = pygame.rect.Rect((0, 0), (Food.SIZE, Food.SIZE))
        self.rect.center = pos

    def render(self, surface):
        pygame.draw.circle(surface, Food.COLOR, self.rect.center, int(Food.SIZE/2))

