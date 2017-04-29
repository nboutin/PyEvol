import pygame
import math
import numpy as np

from color import *
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

    POWER_MIN = 0
    ENGINE_ANGLE = math.radians(45)
    SPEED_STEP = 0.2

    id = 0

    def __init__(self, pos):
        self.rect = pygame.rect.Rect((0,0), (Creature.SIZE, Creature.SIZE))
        self.rect.center = pos
        self.theta = math.radians(0) # radians
        self.color = GREEN

        (self.left_power, self.right_power) = (0,0)

        self.nn = NeuralNetwork(2,2)
        self.is_human_controlled = False
        self._is_selected = False

        self.calorie = 20

    @property
    def is_selected(self):
        return self._is_selected

    @is_selected.setter
    def is_selected(self, bool):
        self._is_selected = bool
        if not bool:
            self.is_human_controlled = False

    def process_inputs(self, events, key_pressed):

        if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_UP]:
            self.right_power += Creature.SPEED_STEP
        else:
            self.right_power = max(self.right_power - Creature.SPEED_STEP, 0)

        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_UP]:
            self.left_power += Creature.SPEED_STEP
        else:
            self.left_power = max(self.left_power - Creature.SPEED_STEP, 0)

    def compute(self, foods):

        eye_left_pos = rotate(self.rect.move(0, -Creature.body_radius).center, self.rect.center, self.theta)
        eye_right_pos = rotate(self.rect.move(0, Creature.body_radius).center, self.rect.center, self.theta)

        left_distances = [distance(eye_left_pos, d.rect.center) for d in foods]
        right_distances = [distance(eye_right_pos, d.rect.center) for d in foods]

        if self.is_human_controlled:
            self.move(self.left_power, self.right_power)
        else:
            inputs = np.matrix([min(left_distances), min(right_distances)])
            powers = self.nn.compute(inputs)
            self.move(powers[0], powers[1])

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
        self.calorie += food.eat(1)

    def render(self, surface):
        # Body
        pygame.draw.circle(surface, self.color, self.rect.center, Creature.body_radius)

        # Eyes
        eye_pos = (self.rect.centerx + Creature.quarter_size, self.rect.centery - Creature.quarter_size)
        eye_pos = rotate(eye_pos, self.rect.center, self.theta)
        pygame.draw.circle(surface, BLACK, eye_pos, Creature.eye_radius)

        eye_pos = (self.rect.centerx + Creature.quarter_size, self.rect.centery + Creature.quarter_size)
        eye_pos = rotate(eye_pos, self.rect.center, self.theta)
        pygame.draw.circle(surface, BLACK, eye_pos, Creature.eye_radius)

        # Selected by mouse click
        if self.is_selected:
            pygame.draw.circle(surface, RED, self.rect.center, Creature.body_radius*2, 1)


