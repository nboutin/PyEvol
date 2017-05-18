import pygame
import pymunk
import pymunk.pygame_util
import numpy as np

import color
import world_scene
from neural_network import NeuralNetwork


class Eye:
    def __init__(self):
        self.pos = pymunk.Vec2d(0, 0)
        self.hit = None


class Creature:
    # pygame
    SIZE = 20
    BODY_RADIUS = int(SIZE / 2)
    EYE_RADIUS = 3
    COLOR_DEFAULT = color.TEAL
    COLOR_BEST = color.RED

    # pymunk
    FORCE = 200
    MASS = 2

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
        self.line_view = pymunk.Segment(self.body, (0, -self.radius), (0, +self.radius), 1)
        q_radius = self.radius / 2
        self.line_eyes = pymunk.Segment(self.body, (q_radius, q_radius), (q_radius, -q_radius), 1)

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

    def compute(self):

        # Eye position
        self.eye_left.pos = self.line_view.a.rotated(self.body.angle) + self.body.position
        self.eye_right.pos = self.line_view.b.rotated(self.body.angle) + self.body.position

        # Find nearest food
        filter_ = pymunk.ShapeFilter(mask=world_scene.categories['food'])
        self.eye_left.hit = self.space.point_query_nearest(self.eye_left.pos, 200, filter_)
        self.eye_right.hit = self.space.point_query_nearest(self.eye_right.pos, 200, filter_)

        # Control
        dl = self.eye_left.hit.distance if self.eye_left.hit else 1000
        dr = self.eye_right.hit.distance if self.eye_right.hit else 1000

        inputs = np.matrix([dl, dr])  # , self.body.velocity.x])#, self.body.velocity.y, self.body.angular_velocity])
        powers = self.nn.compute(inputs)

        # Apply force
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

        # Body
        pygame.draw.circle(surface, self.color, self.rect.center, Creature.BODY_RADIUS)

        # Eyes
        a = self.body.position + self.line_eyes.a.rotated(self.body.angle)
        b = self.body.position + self.line_eyes.b.rotated(self.body.angle)
        a = pymunk.pygame_util.to_pygame(a, surface)
        b = pymunk.pygame_util.to_pygame(b, surface)
        pygame.draw.circle(surface, color.BLACK, a, Creature.EYE_RADIUS)
        pygame.draw.circle(surface, color.BLACK, b, Creature.EYE_RADIUS)

        # Food label
        label = self.font.render("{:2.1f}".format(self.food), 1, color.BLACK)
        surface.blit(label, self.rect.midbottom)

        # Eye sight
        if self.eye_left.hit:
            p = pymunk.pygame_util.to_pygame(self.eye_left.pos, surface)
            p2 = pymunk.pygame_util.to_pygame(self.eye_left.hit.point, surface)
            pygame.draw.line(surface, color.PURPLE, p, p2)

        if self.eye_right.hit:
            p = pymunk.pygame_util.to_pygame(self.eye_right.pos, surface)
            p2 = pymunk.pygame_util.to_pygame(self.eye_right.hit.point, surface)
            pygame.draw.line(surface, color.PURPLE, p, p2)

        # Line direction and eye
        # self.draw_line(self.line_dir, surface, color.BLACK)
        # self.draw_line(self.line_view, surface, color.BLACK)
        # self.draw_line(self.line_eyes, surface, color.BLACK)

        # Selected by mouse click
        if self.is_selected:
            pygame.draw.circle(surface, color.RED, self.rect.center, Creature.BODY_RADIUS * 2, 1)

    def draw_line(self, line, surface, color_):
        a = self.body.position + line.a.rotated(self.body.angle)
        b = self.body.position + line.b.rotated(self.body.angle)
        a = pymunk.pygame_util.to_pygame(a, surface)
        b = pymunk.pygame_util.to_pygame(b, surface)
        pygame.draw.line(surface, color_, a, b, 1)
