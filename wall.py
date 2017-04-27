import pygame

from color import *


class Wall():

    WIDTH = 10

    def __init__(self, rect):
        self.rect = rect

    def render(self, surface):
        pygame.draw.rect(surface, BLACK, self.rect, Wall.WIDTH)
