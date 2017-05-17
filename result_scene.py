import pygame

from scene_base import SceneBase
import main_scene
import simulation_scene
from model import SimulationModel
from color import *


class ResultScene(SceneBase):

    def __init__(self, screen_rect, model):
        SceneBase.__init__(self)
        self.rect = screen_rect
        self.surface = pygame.Surface(self.rect.size)
        self.font = pygame.font.SysFont("monospace", 15)

        self.model = model
        self.simu_model = model.simulation
        self.on_update = True

    def process_input(self, events, key_pressed):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.simu_model.state = SimulationModel.State.EXIT
                    self.on_update = True
                elif event.key == pygame.K_RETURN: # Enter
                    self.simu_model.state = SimulationModel.State.CONTINUE
                    self.on_update = True

    def compute(self):

        if self.on_update:
            self.on_update = False

            if self.simu_model.state == SimulationModel.State.START:
                self.simu_model.state = SimulationModel.State.CONTINUE
                self.simu_model.construct()
                self.switch_to_scene(simulation_scene.SimulationScene(self.rect, self.model))

            elif self.simu_model.state == SimulationModel.State.CONTINUE:
                self.simu_model.ga.compute()
                self.switch_to_scene(simulation_scene.SimulationScene(self.rect, self.model))

            elif self.simu_model.state == SimulationModel.State.EXIT:
                self.switch_to_scene(main_scene.MainScene(self.rect, self.model))

    def render(self, surface):
        self.surface.fill(LIGHT_SEA_GREEN)

        label = self.font.render("Enter: Start simulation", 1, BLACK)
        self.surface.blit(label, (10, 10))

        label = self.font.render("Escape: Go to main menu", 1, BLACK)
        self.surface.blit(label, (10, 30))

        surface.blit(self.surface, (0, 0))
