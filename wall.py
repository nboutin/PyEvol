import pygame

import color


class Wall:

    WIDTH = 10
    COLOR = color.BLACK

    def __init__(self, rect):
        self.rect = rect

    def render(self, surface):
        pygame.draw.rect(surface, Wall.COLOR, self.rect, Wall.WIDTH)

    @property
    def border_right(self):
        return pygame.rect.Rect(self.rect.topright, (1, self.rect.h))

    @property
    def border_left(self):
        return pygame.rect.Rect(self.rect.topleft, (1, self.rect.h))

    @property
    def border_top(self):
        return pygame.rect.Rect(self.rect.topleft, (self.rect.w, 1))

    @property
    def border_bottom(self):
        return pygame.rect.Rect(self.rect.bottomleft, (self.rect.w, 1))