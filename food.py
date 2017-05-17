import pygame
import pymunk
import pymunk.pygame_util

import color
import world_scene


class Food:

    COLOR = color.YELLOW

    def __init__(self, pos, space):

        self.calories = 20
        size = self.calories * 2
        self.rect = pygame.rect.Rect((0, 0), (size, size))

        self.space = space
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = pos
        radius = size / 2
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.sensor = True
        self.shape.collision_type = world_scene.collision_types['food']
        self.space.add(self.shape)

    def __del__(self):
        # remove from space
        self.space.remove(self.shape)

    def eat(self, q):
        if self.calories - q > 0:
            self.calories -= q
            self.shape.unsafe_set_radius(self.shape.radius - 2 * q)
            return q
        else:
            tmp = self.calories
            self.calories = 0
            return tmp

    def render(self, surface):
        self.rect.center = pymunk.pygame_util.to_pygame(self.body.position, surface)
        pygame.draw.circle(surface, Food.COLOR, self.rect.center, int(self.calories))
