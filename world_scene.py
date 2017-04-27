import pygame
import numpy as np

from scene_base import SceneBase
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
        self.rect = pygame.rect.Rect(0, 0, 1200, 1200)
        self.surface = pygame.surface.Surface(self.rect.size)

        self.creatures = list()
        for i in range(0, 50):
            self.creatures.append(Creature(self.rect.center))
        self.creature_selected = None

        self.wall = Wall(self.rect)

        self.foods = list()
        for i in range(0, 10):
            self.foods.append(Food((np.random.randint(0, self.rect.width), np.random.randint(0, self.rect.height))))

        (self.move_x, self.move_y) = (0,0)
        self.zoom = 1
        self.camera_pos = [0, 0]
        self.mouse_click_pos = None

        (self.left_power, self.right_power) = (0,0)

    def process_input(self, events, key_pressed):

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
                if event.key == pygame.K_q:
                    self.move_x += WorldScene.MOVE_STEP
                elif event.key == pygame.K_d:
                    self.move_x += -WorldScene.MOVE_STEP
                elif event.key == pygame.K_z:
                    self.move_y += WorldScene.MOVE_STEP
                elif event.key == pygame.K_s:
                    self.move_y += -WorldScene.MOVE_STEP

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                    self.mouse_click_pos = pygame.mouse.get_pos()
                    # move_x = copy_screen_size[0] / 2 - mouse[0]
                    # move_y = copy_screen_size[1] / 2 - mouse[1]
                if event.button == 4:
                    self.zoom += WorldScene.ZOOM_STEP
                elif event.button == 5:
                    self.zoom -= WorldScene.ZOOM_STEP

    def compute(self):

        if self.mouse_click_pos:
            creature_clicked = [creature for creature in self.creatures if creature.rect.collidepoint(self.mouse_click_pos)]
            self.mouse_click_pos = None

            if creature_clicked:
                if not self.creature_selected:
                    self.creature_selected = creature_clicked.pop()
                    self.creature_selected.is_human_controlled = True
                    self.creatures.pop(self.creatures.index(self.creature_selected))
                else:
                    self.creature_selected.is_human_controlled = False
                    self.creatures.append(self.creature_selected)

                    self.creature_selected = creature_clicked.pop()
                    self.creature_selected.is_human_controlled = True
                    self.creatures.pop(self.creatures.index(self.creature_selected))
            else:
                if self.creature_selected:
                    self.creature_selected.is_human_controlled = False
                    self.creatures.append(self.creature_selected)
                    self.creature_selected = None

        if self.creature_selected:
            self.creature_selected.move(self.left_power, self.right_power)

        # Creatures
        for creature in self.creatures:
            creature.compute(self.foods)

        # Camera
        self.camera_pos[0] = self.rect.width / 2 - self.rect.width / 2 * self.zoom
        self.camera_pos[1] = self.rect.height / 2 - self.rect.height / 2 * self.zoom

        self.camera_pos[0] += self.move_x
        self.camera_pos[1] += self.move_y

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
        # pygame.draw.circle(self.surface, RED, self.target_pos, 10)

        # Creatures
        if self.creature_selected:
            self.creature_selected.render(self.surface)

        for creature in self.creatures:
            creature.render(self.surface)

        # Blit to surface
        pos = [int(i * self.zoom) for i in self.rect.size]
        surface.fill(WHITE)
        surface.blit(pygame.transform.scale(self.surface, pos), self.camera_pos)

    def terminate(self):
        pass
