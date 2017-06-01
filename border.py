import pygame
import pymunk

import color
import world_scene


class Border:

    WIDTH = 10
    COLOR = color.BLUE

    def __init__(self, rect, space):
        self.rect = rect

        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = rect.topleft

        self.lines = list()
        self.lines.append(pymunk.Segment(body, rect.topleft, rect.topright, Border.WIDTH))
        self.lines.append(pymunk.Segment(body, rect.bottomleft, rect.bottomright, Border.WIDTH))
        self.lines.append(pymunk.Segment(body, rect.topleft, rect.bottomleft, Border.WIDTH))
        self.lines.append(pymunk.Segment(body, rect.topright, rect.bottomright, Border.WIDTH))

        for l in self.lines:
            l.filter = pymunk.ShapeFilter(categories=world_scene.categories['border'])

        space.add(self.lines)
        self.space = space

    def __del__(self):
        self.space.remove(self.lines)

    def render(self, surface):
        pygame.draw.rect(surface, Border.COLOR, self.rect, Border.WIDTH)
