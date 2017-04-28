import pygame
import numpy as np

from scene_base import SceneBase
from camera import Camera
from color import *
from creature import Creature
from wall import Wall
from food import Food


class WorldScene(SceneBase):

    #size
    MOVE_STEP = 100
    ZOOM_STEP = 0.2
    SPEED_STEP = 0.2

    def __init__(self):
        # Drawing
        self.rect = pygame.rect.Rect(0, 0, 1200, 1200)
        self.surface = pygame.surface.Surface(self.rect.size)
        self.camera = Camera(self.rect)
        self.mouse_click_pos = None

        # World Objects
        self.creatures = list()
        for i in range(0, 50):
            self.creatures.append(Creature(self.rect.center))
        self.creature_selected = None

        self.wall = Wall(self.rect)

        self.foods = list()
        for i in range(0, 10):
            self.foods.append(Food((np.random.randint(0, self.rect.width), np.random.randint(0, self.rect.height))))

        # Control
        (self.left_power, self.right_power) = (0,0)

    def process_input(self, events, key_pressed):

        self.camera.process_input(events)

        if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_UP]:
            self.right_power += WorldScene.SPEED_STEP
        else:
            self.right_power = max(self.right_power - WorldScene.SPEED_STEP, 0)

        if key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_UP]:
            self.left_power += WorldScene.SPEED_STEP
        else:
            self.left_power = max(self.left_power - WorldScene.SPEED_STEP, 0)

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
            creature_clicked = [creature for creature in self.creatures if creature.rect.collidepoint(self.mouse_click_pos)]
            self.mouse_click_pos = None

            if creature_clicked:
                if not self.creature_selected:
                    self.creature_selected = creature_clicked.pop()
                    self.creature_selected.is_selected = True
                    self.creatures.pop(self.creatures.index(self.creature_selected))
                else:
                    self.creature_selected.is_human_controlled = False
                    self.creature_selected.is_selected = False
                    self.creatures.append(self.creature_selected)

                    self.creature_selected = creature_clicked.pop()
                    self.creature_selected.is_selected = True
                    self.creatures.pop(self.creatures.index(self.creature_selected))
            else:
                if self.creature_selected:
                    self.creature_selected.is_selected = False
                    self.creature_selected.is_human_controlled = False
                    self.creatures.append(self.creature_selected)
                    self.creature_selected = None

        if self.creature_selected:
            if self.creature_selected.is_human_controlled:
                self.creature_selected.move(self.left_power, self.right_power)
            else:
                self.creature_selected.compute(self.foods)

        # Creatures
        for creature in self.creatures:
            creature.compute(self.foods)

    def render(self, surface):

        # Background
        self.surface.fill(LIGHT_GRAY)

        # Center
        pygame.draw.circle(self.surface, BLACK, self.rect.center, 50, 5)

        # Wall
        self.wall.render(self.surface)

        # Food
        for food in self.foods:
            food.render(self.surface)

        # Creatures
        if self.creature_selected:
            self.creature_selected.render(self.surface)

        for creature in self.creatures:
            creature.render(self.surface)

        # Blit to surface
        surface.fill(WHITE)
        surface.blit(pygame.transform.scale(self.surface, self.camera.area.size), self.camera.area.topleft)

    def terminate(self):
        pass
