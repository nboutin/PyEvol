import pygame
import pymunk
import pymunk.pygame_util

import color
import constants


class Food:
    COLOR = color.YELLOW
    RADIUS_MIN = 5
    MASS = 200

    def __init__(self, pos, space):

        self.calories = 20
        size = self.calories * 2
        self.rect = pygame.rect.Rect((0, 0), (size, size))
        radius = int(size / 2)

        self.space = space
        moment = pymunk.moment_for_circle(Food.MASS, 0, radius)
        self.body = pymunk.Body(Food.MASS, moment)
        self.body.position = pos

        self.shape = pymunk.Circle(self.body, radius)
        # self.shape.sensor = True
        self.shape.collision_type = constants.collision_types['food']
        self.shape.filter = pymunk.ShapeFilter(categories=constants.categories['food'])
        self.space.add(self.body, self.shape)

    # def __del__(self):
    #     self.space.remove(self.body, self.shape)

    def eat(self, q):
        if self.calories - q > 0:
            self.calories -= q
            self.shape.unsafe_set_radius(max(self.shape.radius - q, Food.RADIUS_MIN))
            return q
        else:
            tmp = self.calories
            self.calories = 0
            return tmp

    def render(self, surface):
        self.rect.center = pymunk.pygame_util.to_pygame(self.body.position, surface)
        pygame.draw.circle(surface, Food.COLOR, self.rect.center, int(self.shape.radius))
