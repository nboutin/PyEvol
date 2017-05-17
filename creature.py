import pygame
import pymunk
import pymunk.pygame_util
import math
import numpy as np

import color
import world_scene
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

class Eye:

    def __init__(self):
        self.pos = (0, 0)
        self.d = 0
        self.f = None


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

    FORCE = 75
    MASS = 5

    def __init__(self, space, pos):
        self.rect = pygame.rect.Rect((0,0), (Creature.SIZE, Creature.SIZE))
        # self.theta = math.radians(0) # radians
        self.color = Creature.COLOR_DEFAULT
        self.eye_left = Eye()
        self.eye_right = Eye()

        self.font = pygame.font.SysFont("monospace", 10)

        # pymunk
        self.radius = Creature.SIZE / 2
        moment = pymunk.moment_for_circle(Creature.MASS, 0, self.radius)

        self.body = pymunk.Body(Creature.MASS, moment)
        self.body.position = pos

        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.collision_type = world_scene.collision_types['creature']
        self.line_dir = pymunk.Segment(self.body, (0, 0), (self.radius, 0), 1)
        self.line_eye = pymunk.Segment(self.body, (0, -self.radius), (0, +self.radius), 1)

        space.add(self.body, self.shape)

        # Neural Net
        self.nn = NeuralNetwork(2,2)

        # Other
        self.is_human_controlled = False
        self._is_selected = False
        self._is_best = False
        self.food = 0

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
        pass

    def compute(self, foods):

        # Eye position
        self.eye_left.pos = self.line_eye.a.rotated(self.body.angle) + self.body.position
        self.eye_right.pos = self.line_eye.b.rotated(self.body.angle) + self.body.position

        # Nearest food
        left = [(distance(self.eye_left.pos, f.body.position), f) for f in foods]
        (self.eye_left.d, self.eye_left.f) = min(left, key=lambda t: t[0])

        right = [(distance(self.eye_right.pos, f.body.position), f) for f in foods]
        (self.eye_right.d, self.eye_right.f) = min(right, key=lambda t: t[0])

        # Control
        inputs = np.matrix([self.eye_left.d, self.eye_right.d])
        powers = self.nn.compute(inputs)

        p1 = powers[0] * Creature.FORCE
        p2 = powers[1] * Creature.FORCE
        self.body.apply_force_at_local_point((p1, 0), (0, -self.radius))
        self.body.apply_force_at_local_point((p2, 0), (0, +self.radius))

    def eat(self, food):
        self.food += food.eat(0.25)

    def render(self, surface):

        self.rect.center = pymunk.pygame_util.to_pygame(self.body.position, surface)
        # self.theta = self.body.angle

        # Body
        pygame.draw.circle(surface, self.color, self.rect.center, Creature.body_radius)

        # Eyes
        # eye_pos = (self.rect.centerx + Creature.quarter_size, self.rect.centery - Creature.quarter_size)
        # eye_pos = rotate(eye_pos, self.rect.center, self.theta)
        # pygame.draw.circle(surface, color.BLACK, eye_pos, Creature.eye_radius)
        #
        # eye_pos = (self.rect.centerx + Creature.quarter_size, self.rect.centery + Creature.quarter_size)
        # eye_pos = rotate(eye_pos, self.rect.center, self.theta)
        # pygame.draw.circle(surface, color.BLACK, eye_pos, Creature.eye_radius)

        # Food
        label = self.font.render("{:2.1f}".format(self.food), 1, color.BLACK)
        surface.blit(label, self.rect.midbottom)

        # Eye sight
        p = pymunk.pygame_util.to_pygame(self.eye_left.pos, surface)
        pygame.draw.line(surface, color.RED, p, self.eye_left.f.rect.center)

        p = pymunk.pygame_util.to_pygame(self.eye_right.pos, surface)
        pygame.draw.line(surface, color.RED, p, self.eye_right.f.rect.center)

        # Line direction and eye
        self.draw_line(self.line_dir, surface, color.BLACK)
        self.draw_line(self.line_eye, surface, color.BLACK)

        # Selected by mouse click
        if self.is_selected:
            pygame.draw.circle(surface, color.RED, self.rect.center, Creature.body_radius*2, 1)

    def draw_line(self, line, surface, color_):
        a = self.body.position + line.a.rotated(self.body.angle)
        b = self.body.position + line.b.rotated(self.body.angle)
        a = pymunk.pygame_util.to_pygame(a, surface)
        b = pymunk.pygame_util.to_pygame(b, surface)
        pygame.draw.line(surface, color_, a, b, 1)



