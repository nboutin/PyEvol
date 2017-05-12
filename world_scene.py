import pygame
import numpy as np
import os.path

import parameters
from scene_base import SceneBase
from camera import Camera
import color
from creature import Creature
from wall import Wall
from food import Food


class WorldScene(SceneBase):

    FOOD_COUNT = 20
    COLOR_BACKGROUND = color.LIGHT_GREEN

    def __init__(self, model):
        # Drawing
        self.rect = pygame.rect.Rect(0, 0, 1050, 1050)
        self.surface = pygame.surface.Surface(self.rect.size)
        self.camera = Camera(self.rect)
        self.mouse_click_pos = None
        # self.grass = pygame.image.load(os.path.join("res", "grass.jpg"))
        # self.grass = pygame.transform.scale(self.grass, self.rect.size)

        # World Objects
        self.model = model
        self.creatures = self.model.creatures

        for c in self.creatures:
            c.set_pos((np.random.randint(0, self.rect.width), np.random.randint(0, self.rect.height)))
        self.creature_selected = None
        self.best = None

        self.wall = Wall(self.rect)

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
            creature.compute(self.foods)

        max = 0
        for creature in self.creatures:
            if creature.food > max:
                max = creature.food
                if self.best:
                    self.best.is_best = False
                self.best = creature
                self.best.is_best = True

        # Check wall collisions
        for creature in self.creatures:
            if creature.rect.colliderect(self.wall.border_right):
                creature.rect.right = self.wall.rect.right

            if creature.rect.colliderect(self.wall.border_left):
                creature.rect.left = self.wall.rect.left

            if creature.rect.colliderect(self.wall.border_top):
                creature.rect.top = self.wall.rect.top

            if creature.rect.colliderect(self.wall.border_bottom):
                creature.rect.bottom = self.wall.rect.bottom

        # Delete depleted foods
        self.foods = [f for f in self.foods if f.calories > 0]
        self.add_foods(WorldScene.FOOD_COUNT - len(self.foods))

    def render(self, surface):

        # Background
        self.surface.fill(WorldScene.COLOR_BACKGROUND)
        # self.surface.blit(self.grass, (0, 0))

        # Food
        for food in self.foods:
            food.render(self.surface)

        # Wall
        self.wall.render(self.surface)


        # Creatures
        if self.creature_selected:
            self.creature_selected.render(self.surface)

        for creature in self.creatures:
            creature.render(self.surface)

        # Blit to surface
        surface.fill(color.WHITE)
        surface.blit(pygame.transform.scale(self.surface, self.camera.area.size), self.camera.area.topleft)
