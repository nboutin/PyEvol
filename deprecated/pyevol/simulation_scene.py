import pygame

import parameters
import main_scene
import result_scene
from scene_base import SceneBase
from world_scene import WorldScene
from info_scene import InfoScene
from model import model
from model import simulation_model


class SimulationScene(SceneBase):

    def __init__(self, rect):
        SceneBase.__init__(self)

        self.surface = pygame.Surface(rect.size)
        self.surface = self.surface.convert()

        r_world = pygame.rect.Rect((0, 0), (rect.h, rect.h))
        self.world_surface = self.surface.subsurface(r_world)
        self.world_scene = WorldScene(r_world)

        info_rect = pygame.rect.Rect((r_world.w, 0), (rect.w - r_world.w, rect.h))
        self.info_surface = self.surface.subsurface(info_rect)
        self.info_scene = InfoScene(self.world_scene)

    def __del__(self):
        print("__del__ SimulationScene")

    def process_input(self, events, key_pressed):

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.switch_to_scene(main_scene.MainScene(self.surface.get_rect()))
                elif event.key == pygame.K_RETURN:
                    self.switch_to_scene(result_scene.ResultScene(self.surface.get_rect()))
                    return

        # End of Simulation
        if simulation_model.time_ms / 1000 >= parameters.SIMULATION_TIME:
            self.switch_to_scene(result_scene.ResultScene(self.surface.get_rect()))
            return

        self.world_scene.process_input(events, key_pressed)
        self.info_scene.process_input(events, key_pressed)

    def compute(self):
        simulation_model.time_ms += model.clock.get_time()

        self.world_scene.compute()
        self.info_scene.compute()

    def render(self, surface):
        self.world_scene.render(self.world_surface)
        self.info_scene.render(self.info_surface)

        surface.blit(self.surface, (0, 0))
