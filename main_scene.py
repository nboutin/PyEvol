import pygame

from scene_base import SceneBase
from simulation_scene import SimulationScene
from color import *


class MainScene(SceneBase):

    def __init__(self, screen_rect, model):
        SceneBase.__init__(self)
        self.rect = screen_rect
        self.surface = pygame.Surface(self.rect.size)
        self.font = pygame.font.SysFont("monospace", 15)

        self.model = model

    def process_input(self, events, key_pressed):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.switch_to_scene(SimulationScene(self.rect, self.model))

    def compute(self):
        pass

    def render(self, surface):
        self.surface.fill(LIGHT_GREEN)

        label = self.font.render("Press Enter to start simulation", 1, BLACK)
        self.surface.blit(label, (10, 10))

        surface.blit(self.surface, (0, 0))
