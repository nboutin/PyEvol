import pygame

import color


class Food:

    COLOR = color.YELLOW

    def __init__(self, pos):
        self.calories = 20
        size = self.calories * 2
        self.rect = pygame.rect.Rect((0, 0), (size, size))
        self.rect.center = pos

    def eat(self, q):
        if self.calories - q > 0:
            self.calories -= q
            # self.rect.size = (self.calories, self.calories)
            self.rect.inflate_ip(q, q)
            return q
        else:
            tmp = self.calories
            self.calories = 0
            return tmp

    def render(self, surface):
        pygame.draw.circle(surface, Food.COLOR, self.rect.center, int(self.calories))
