import pygame
import pymunk
import pymunk.pygame_util
import math
import numpy as np

import color
import world_scene
from neural_network import NeuralNetwork


class Eye:
    def __init__(self):
        self.pos = pymunk.Vec2d(0, 0)
        self.d = 0
        self.f = None
        self.hit = None


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

    FORCE = 150
    MASS = 5

    def __init__(self, space, pos):
        self.rect = pygame.rect.Rect((0, 0), (Creature.SIZE, Creature.SIZE))
        self.color = Creature.COLOR_DEFAULT
        self.eye_left = Eye()
        self.eye_right = Eye()

        self.font = pygame.font.SysFont("monospace", 10)

        # pymunk
        self.space = space
        self.radius = Creature.SIZE / 2
        moment = pymunk.moment_for_circle(Creature.MASS, 0, self.radius)

        self.body = pymunk.Body(Creature.MASS, moment)
        self.body.position = pos

        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.collision_type = world_scene.collision_types['creature']
        self.shape.filter = pymunk.ShapeFilter(categories=world_scene.categories['creature'])
        self.line_dir = pymunk.Segment(self.body, (0, 0), (self.radius, 0), 1)
        self.line_eye = pymunk.Segment(self.body, (0, -self.radius), (0, +self.radius), 1)

        space.add(self.body, self.shape)

        # Neural Net
        self.nn = NeuralNetwork(2, 2)

        # Other
        self.is_human_controlled = False
        self._is_selected = False
        self._is_best = False
        self.food = 0

    @property
    def is_selected(self):
        return self._is_selected

    @is_selected.setter
    def is_selected(self, s):
        self._is_selected = s
        if not s:
            self.is_human_controlled = False

    @property
    def is_best(self):
        return self._is_best

    @is_best.setter
    def is_best(self, b):
        self._is_best = b
        if b:
            self.color = Creature.COLOR_BEST
        else:
            self.color = Creature.COLOR_DEFAULT

    def process_inputs(self, events, key_pressed):
        pass

    def compute(self, foods):

        # Eye position
        self.eye_left.pos = self.line_eye.a.rotated(self.body.angle) + self.body.position
        self.eye_right.pos = self.line_eye.b.rotated(self.body.angle) + self.body.position

        filter_ = pymunk.ShapeFilter(mask=world_scene.categories['food'])
        self.eye_left.hit = self.space.point_query_nearest(self.eye_left.pos, 200, filter_)
        self.eye_right.hit = self.space.point_query_nearest(self.eye_right.pos, 200, filter_)

        # Nearest food
        # left = [(self.eye_left.pos.get_distance(f.body.position), f) for f in foods]
        # (self.eye_left.d, self.eye_left.f) = min(left, key=lambda t: t[0])
        #
        # if self.eye_left.hit:
        #     print(self.eye_left.hit.distance, self.eye_left.d)
        # else:
        #     print("not hit")
        #
        # right = [(self.eye_right.pos.get_dist_sqrd(f.body.position), f) for f in foods]
        # (self.eye_right.d, self.eye_right.f) = min(right, key=lambda t: t[0])

        # Control
        if self.eye_left.hit:
            dl = self.eye_left.hit.distance
        else:
            dl = 1000

        if self.eye_right.hit:
            dr = self.eye_right.hit.distance
        else:
            dr = 1000

        inputs = np.matrix([dl, dr])#, self.body.velocity.x])#, self.body.velocity.y, self.body.angular_velocity])
        powers = self.nn.compute(inputs)

        # 1
        p1 = powers[0] * Creature.FORCE
        p2 = powers[1] * Creature.FORCE
        self.body.apply_force_at_local_point((p1, 0), (0, -self.radius))
        self.body.apply_force_at_local_point((p2, 0), (0, +self.radius))

        # 2
        # p1x = powers[0] * Creature.FORCE
        # p1y = powers[1] * Creature.FORCE
        # p2x = powers[2] * Creature.FORCE
        # p2y = powers[3] * Creature.FORCE
        # self.body.apply_force_at_local_point((p1x, p1y), self.eye_left.pos)
        # self.body.apply_force_at_local_point((p2x, p2y), self.eye_right.pos)

    def eat(self, food):
        self.food += food.eat(0.50)

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

        # Food label
        label = self.font.render("{:2.1f}".format(self.food), 1, color.BLACK)
        surface.blit(label, self.rect.midbottom)

        # Eye sight
        # p = pymunk.pygame_util.to_pygame(self.eye_left.pos, surface)
        # pygame.draw.line(surface, color.RED, p, self.eye_left.f.rect.center)
        # p = pymunk.pygame_util.to_pygame(self.eye_right.pos, surface)
        # pygame.draw.line(surface, color.RED, p, self.eye_right.f.rect.center)

        if self.eye_left.hit:
            p = pymunk.pygame_util.to_pygame(self.eye_left.pos, surface)
            p2 = pymunk.pygame_util.to_pygame(self.eye_left.hit.point, surface)
            pygame.draw.line(surface, color.PURPLE, p, p2)

        if self.eye_right.hit:
            p = pymunk.pygame_util.to_pygame(self.eye_right.pos, surface)
            p2 = pymunk.pygame_util.to_pygame(self.eye_right.hit.point, surface)
            pygame.draw.line(surface, color.PURPLE, p, p2)

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
