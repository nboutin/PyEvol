import pygame
import pymunk
import numpy as np

from scene_base import SceneBase
from camera import Camera
import color
from border import Border
from food import Food


class WorldScene(SceneBase): # needed ?

    FOOD_COUNT = 20
    COLOR_BACKGROUND = color.LIGHT_GREEN

    def __init__(self, simu_model):
        # Model
        self.simu_model = simu_model
        self.rect = simu_model.rect
        self.space = simu_model.space

        # Drawing
        self.surface = pygame.surface.Surface(self.rect.size)
        self.surface = self.surface.convert()
        self.camera = Camera(self.rect)
        self.mouse_click_pos = None

        self.border = Border(self.rect, self.space)

        # World Objects
        self.creatures = simu_model.creatures

        self.creature_selected = None
        self.best = None

        self.foods = list()
        self.add_foods(WorldScene.FOOD_COUNT)

    def __del__(self):
        if self.best:
            self.best.is_best = False

        if self.creature_selected:
            self.creature_selected.is_selected = False

    def add_foods(self, n):
        for i in range(0, n):
            self.foods.append(Food((np.random.randint(0, self.rect.width), np.random.randint(0, self.rect.height))))

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
            creature.compute(self.simu_model.delta_time, self.foods)

        _max = 0
        for creature in self.creatures:
            if creature.food > _max:
                _max = creature.food
                if self.best:
                    self.best.is_best = False
                self.best = creature
                self.best.is_best = True

        # Delete depleted foods
        self.foods = [f for f in self.foods if f.calories > 0]
        self.add_foods(WorldScene.FOOD_COUNT - len(self.foods))

        # self.simu_model.space.step(1/30.0)
        self.simu_model.space.step(1 / self.simu_model.clock.get_fps())

    def render(self, surface):

        # Background
        self.surface.fill(WorldScene.COLOR_BACKGROUND)
        # self.surface.blit(self.grass, (0, 0))

        # Food
        for food in self.foods:
            food.render(self.surface)

        # Wall
        self.border.render(self.surface)

        # Creatures
        if self.creature_selected:
            self.creature_selected.render(self.surface)

        for creature in self.creatures:
            creature.render(self.surface)

        # Blit to surface
        surface.fill(color.WHITE)
        surface.blit(pygame.transform.scale(self.surface, self.camera.area.size), self.camera.area.topleft)
