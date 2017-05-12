import pygame

from scene_base import SceneBase
import main_scene
import simulation_scene
from color import *


class ResultScene(SceneBase):

    def __init__(self, screen_rect, model):
        SceneBase.__init__(self)
        self.rect = screen_rect
        self.surface = pygame.Surface(self.rect.size)
        self.font = pygame.font.SysFont("monospace", 15)

        self.model = model

        self.one_time = True

    def process_input(self, events, key_pressed):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: # Enter
                    self.switch_to_scene(simulation_scene.SimulationScene(self.rect, self.model))
                elif event.key == pygame.K_ESCAPE:
                    self.switch_to_scene(main_scene.MainScene(self.rect, self.model))

    def compute(self):
        if self.one_time:
            self.one_time = False

            self.model.ga.compute()

            pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN))

    def render(self, surface):
        self.surface.fill(LIGHT_BLUE)

        label = self.font.render("Enter: Start simulation", 1, BLACK)
        self.surface.blit(label, (10, 10))

        label = self.font.render("Escape: Go to main menu", 1, BLACK)
        self.surface.blit(label, (10, 30))

        surface.blit(self.surface, (0, 0))
