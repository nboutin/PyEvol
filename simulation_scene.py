import pygame

import parameters
import main_scene
import result_scene
from scene_base import SceneBase
from world_scene import WorldScene
from info_scene import InfoScene


class SimulationScene(SceneBase):

    def __init__(self, screen_rect, model):
        SceneBase.__init__(self)

        self.model = model
        self.model.simulation_time_ms = 0

        self.rect = screen_rect
        self.surface = pygame.Surface(self.rect.size)
        self.surface = self.surface.convert()

        world_rect = pygame.rect.Rect((0, 0), (self.rect.h, self.rect.h))
        self.world_surface = self.surface.subsurface(world_rect)
        # self.world_surface = self.world_surface.convert()
        self.world_scene = WorldScene(self.model)

        info_rect = ((world_rect.w, 0), (self.rect.w - world_rect.w, self.rect.h))
        self.info_surface = self.surface.subsurface(info_rect)
        # self.info_surface = self.info_surface.convert()
        self.info_scene = InfoScene(self.world_scene, self.model)

    def process_input(self, events, key_pressed):

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.switch_to_scene(main_scene.MainScene(self.rect, self.model))
                elif event.key == pygame.K_RETURN:
                    self.switch_to_scene(result_scene.ResultScene(self.rect, self.model))
                    return

        # End of Simulation
        if self.model.simulation_time_ms / 1000 >= parameters.SIMULATION_TIME:
            self.switch_to_scene(result_scene.ResultScene(self.rect, self.model))
            return

        self.world_scene.process_input(events, key_pressed)
        self.info_scene.process_input(events, key_pressed)

    def compute(self):
        self.model.simulation_time_ms += self.model.clock.get_time()

        self.world_scene.compute()
        self.info_scene.compute()

    def render(self, surface):
        self.world_scene.render(self.world_surface)
        self.info_scene.render(self.info_surface)

        surface.blit(self.surface, (0,0))