import pygame
import pymunk

import color


class Border:

    WIDTH = 5
    COLOR = color.BLUE

    def __init__(self, rect, space):
        self.rect = rect

        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = rect.topleft

        lines = list()
        lines.append(pymunk.Segment(body, rect.topleft, rect.topright, Border.WIDTH))
        lines.append(pymunk.Segment(body, rect.bottomleft, rect.bottomright, Border.WIDTH))
        lines.append(pymunk.Segment(body, rect.topleft, rect.bottomleft, Border.WIDTH))
        lines.append(pymunk.Segment(body, rect.topright, rect.bottomright, Border.WIDTH))
        space.add(lines)

    def render(self, surface):
        pygame.draw.rect(surface, Border.COLOR, self.rect, Border.WIDTH)
