import pygame
import pymunk
import numpy as np

import parameters
from camera import Camera
import color
from border import Border
from food import Food
from model import model
from model import simulation_model
import constants


class WorldScene:
    COLOR_BACKGROUND = color.LIGHT_GREEN

    def __init__(self, rect):
        # Model
        self.r_world = simulation_model.r_world
        self.space = simulation_model.space

        # Drawing
        self.s_world = pygame.surface.Surface(self.r_world.size)
        self.s_world = self.s_world.convert()
        self.camera = Camera(self.r_world, rect)
        self.mouse_click_pos = None

        self.border = Border(self.r_world, self.space)

        # World Objects
        self.creatures = simulation_model.creatures

        self.creature_selected = None
        self.best = None
        self.is_follow_best = False

        self.foods = list()
        self.add_foods(parameters.N_FOOD)

        handler_creature_food = self.space.add_collision_handler(
            constants.collision_types["creature"],
            constants.collision_types["food"])

        handler_creature_food.pre_solve = self.creature_eat_food
        handler_creature_food.data['creatures'] = self.creatures
        handler_creature_food.data['foods'] = self.foods

    def __del__(self):
        for f in self.foods:
            self.space.remove(f.shape, f.body)

        if self.best:
            self.best.is_best = False

        if self.creature_selected:
            self.creature_selected.is_selected = False

    @staticmethod
    def creature_eat_food(arbiter, space, data):
        creature_shape = arbiter.shapes[0]
        food_shape = arbiter.shapes[1]

        c = next((c for c in data['creatures'] if c.shape == creature_shape), None)
        f = next((f for f in data['foods'] if f.shape == food_shape), None)

        if c and f:
            c.eat(f)

            if not f.calories > 0:
                space.remove(food_shape, food_shape.body)
                data['foods'].remove(f)
        else:
            pass
            # print("creature_eat_food error {} {}".format(c, f))
        return False  # Workaround to emulate food.shape.sensor=True

    def add_foods(self, n):
        for i in range(0, n):
            pos = (np.random.randint(0, self.r_world.width), np.random.randint(0, self.r_world.height))

            # Do create food on creature
            filter_ = pymunk.ShapeFilter(mask=constants.categories['creature'])
            if not self.space.point_query_nearest(pos, 20, filter_):
                self.foods.append(Food(pos, self.space))
            else:
                i -= 1

    def process_input(self, events, key_pressed):

        self.camera.process_input(events)

        if self.creature_selected:
            self.creature_selected.process_inputs(events, key_pressed)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.creature_selected:
                        if not self.creature_selected.is_human_controlled:
                            self.creature_selected.is_human_controlled = True
                        else:
                            self.creature_selected.is_human_controlled = False
                if event.key == pygame.K_b:
                    if not self.is_follow_best:
                        self.is_follow_best = True
                    else:
                        self.is_follow_best = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse_click_pos = pygame.mouse.get_pos()

    def compute(self):

        if self.mouse_click_pos:
            creature_clicked = [c for c in self.creatures if c.rect.collidepoint(self.mouse_click_pos)]
            self.mouse_click_pos = None

            if creature_clicked:
                if not self.creature_selected:
                    self.creature_selected = creature_clicked[-1]
                    self.creature_selected.is_selected = True
                else:
                    self.creature_selected.is_selected = False
                    self.creature_selected = creature_clicked[-1]
                    self.creature_selected.is_selected = True
            else:
                if self.creature_selected:
                    self.creature_selected.is_selected = False
                    self.creature_selected = None

        # Creatures
        for creature in self.creatures:
            creature.compute()

        _max = 0
        for creature in self.creatures:
            if creature.food > _max:
                _max = creature.food
                if self.best:
                    self.best.is_best = False
                self.best = creature
                self.best.is_best = True

        # A add missing foods
        self.add_foods(parameters.N_FOOD - len(self.foods))

        # self.simu_model.space.step(1.0 / parameters.FPS)
        simulation_model.space.step(1.0 / model.clock.get_fps())

    def render(self, surface):

        # Background
        self.s_world.fill(WorldScene.COLOR_BACKGROUND)

        # Food
        for food in self.foods:
            food.render(self.s_world)

        # Wall
        self.border.render(self.s_world)

        # Creatures
        if self.creature_selected:
            self.creature_selected.render(self.s_world)

        for creature in self.creatures:
            creature.render(self.s_world)

        # Camera
        if self.best and self.is_follow_best:
            center = pymunk.pygame_util.to_pygame(self.best.body.position, surface)
            self.camera.center_at(center)

        # Blit to surface
        surface.fill(color.WHITE)
        surface.blit(self.camera.get_surface(self.s_world), surface.get_rect().topleft, self.camera.area)
