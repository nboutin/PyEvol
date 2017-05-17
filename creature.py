import pygame
import pymunk
import pymunk.pygame_util
import math
import numpy as np

import color
from neural_network import NeuralNetwork


def polar_to_cartesian(r, theta):
    '''r: vector magnitude
    theta: vector direction (radians)
    return: (x,y) cartesian coordinates'''

    return r * math.cos(theta), r * math.sin(theta)


def rotate(point, pivot, angle):
    '''px, py: pivot point
    angle : radians'''

    c = math.cos(angle)
    s = math.sin(angle)

    (px, py) = pivot
    (x, y) = point

    x -= px
    y -= py

    x_new = x * c - y * s
    y_new = x * s + y * c

    return int(x_new + px), int(y_new + py)


def distance(pos, target):
    return math.sqrt(math.pow(target[0] - pos[0], 2) + math.pow(target[1] - pos[1], 2))


class Creature:

    SIZE = 20
    body_radius = int(SIZE / 2)

    half_size = int(SIZE / 2)
    quarter_size = int(SIZE / 4)
    body_draw_pos = (int(SIZE / 2), int(SIZE / 2))
    eye_radius = 3
    eye_left_pos = (int(SIZE * 3 / 4), int(SIZE / 2 - SIZE / 4))
    eye_right_pos = (int(SIZE * 3 / 4), int(SIZE / 2 + SIZE / 4))

    COLOR_DEFAULT = color.TEAL
    COLOR_BEST = color.RED

    POWER_MIN = 0
    ENGINE_ANGLE = math.radians(45)
    SPEED_STEP = 0.2
    K_SPEED = 100
    K1_SPEED = 50

    def __init__(self, space):
        self.rect = pygame.rect.Rect((0,0), (Creature.SIZE, Creature.SIZE))
        self.theta = math.radians(0) # radians
        self.color = Creature.COLOR_DEFAULT
        self.font = pygame.font.SysFont("monospace", 10)

        (self.left_power, self.right_power) = (0,0)

        # pymunk
        mass = 1
        self.radius = Creature.SIZE / 2
        moment = pymunk.moment_for_circle(mass, 0, self.radius)
        self.body = pymunk.Body(mass, moment)
        self.shape = pymunk.Circle(self.body, self.radius)
        self.line = pymunk.Segment(self.body, (0,0), (self.radius,0), 5)
        space.add(self.body, self.shape)

        # Neural Net
        self.nn = NeuralNetwork(2,2)
        self.is_human_controlled = False
        self._is_selected = False
        self._is_best = False

        self.food = 0

    def set_pos(self, pos):
        self.body.position = pos
        self.rect.center = pos

    @property
    def is_selected(self):
        return self._is_selected

    @is_selected.setter
    def is_selected(self, bool):
        self._is_selected = bool
        if not bool:
            self.is_human_controlled = False

    @property
    def is_best(self):
        return self._is_best

    @is_best.setter
    def is_best(self, bool):
        self._is_best = bool
        if bool:
            self.color = Creature.COLOR_BEST
        else:
            self.color = Creature.COLOR_DEFAULT

    def process_inputs(self, events, key_pressed):

        if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_UP]:
            self.right_power += Creature.SPEED_STEP
        else:
            self.right_power = max(self.right_power - Creature.SPEED_STEP, 0)

        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_UP]:
            self.left_power += Creature.SPEED_STEP
        else:
            self.left_power = max(self.left_power - Creature.SPEED_STEP, 0)

    def compute(self, delta_time, foods):

        eye_left_pos = rotate(self.rect.move(0, -Creature.body_radius).center, self.rect.center, self.theta)
        eye_right_pos = rotate(self.rect.move(0, Creature.body_radius).center, self.rect.center, self.theta)

        left_distances = [distance(eye_left_pos, d.rect.center) for d in foods]
        right_distances = [distance(eye_right_pos, d.rect.center) for d in foods]

        if self.is_human_controlled:
            self.move(self.left_power, self.right_power)
        else:
            inputs = np.matrix([min(left_distances), min(right_distances)])
            powers = self.nn.compute(inputs)

            # delta_speed = delta_time * Creature.K_SPEED / 1000.0
            # self.move(powers[0] * delta_speed, powers[1] * delta_speed)

            self.body.apply_force_at_local_point((powers[0] * Creature.K1_SPEED, 0), (0, -self.radius))
            self.body.apply_force_at_local_point((powers[1] * Creature.K1_SPEED, 0), (0, +self.radius))

        #     self.rect =
        #
        # Detect food collision
        for food in foods:
            if self.rect.colliderect(food.rect):
                self.eat(food)

    def move(self, left_power, right_power):

        self.left_power = max(left_power, Creature.POWER_MIN)
        self.right_power = max(right_power, Creature.POWER_MIN)

        (x_l, y_l) = polar_to_cartesian(self.left_power, self.theta + Creature.ENGINE_ANGLE)
        (x_r, y_r) = polar_to_cartesian(self.right_power, self.theta - Creature.ENGINE_ANGLE)

        x_result = x_l + x_r
        y_result = y_l + y_r

        self.rect.x += int(x_result)
        self.rect.y += int(y_result)

        if self.left_power != 0 or self.right_power != 0:
            self.theta = math.atan2(y_result, x_result)

    def eat(self, food):
        self.food += food.eat(0.25)

    def render(self, surface):

        self.rect.center = pymunk.pygame_util.to_pygame(self.body.position, surface)
        self.theta = self.body.angle

        # Body
        pygame.draw.circle(surface, self.color, self.rect.center, Creature.body_radius)

        # Eyes
        eye_pos = (self.rect.centerx + Creature.quarter_size, self.rect.centery - Creature.quarter_size)
        eye_pos = rotate(eye_pos, self.rect.center, self.theta)
        pygame.draw.circle(surface, color.BLACK, eye_pos, Creature.eye_radius)

        eye_pos = (self.rect.centerx + Creature.quarter_size, self.rect.centery + Creature.quarter_size)
        eye_pos = rotate(eye_pos, self.rect.center, self.theta)
        pygame.draw.circle(surface, color.BLACK, eye_pos, Creature.eye_radius)

        # Food
        label = self.font.render("{:2.1f}".format(self.food), 1, color.BLACK)
        surface.blit(label, self.rect.bottomright)


        # Selected by mouse click
        if self.is_selected:
            pygame.draw.circle(surface, color.RED, self.rect.center, Creature.body_radius*2, 1)

        # if self.is_best:
        #     pygame.draw.circle(surface, color.BLUE, self.rect.center, Creature.body_radius * 2, 2)


