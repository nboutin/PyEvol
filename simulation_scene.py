import pygame

from scene_base import SceneBase
import main_scene
from world_scene import WorldScene
from info_scene import InfoScene


class SimulationScene(SceneBase):

    def __init__(self, screen_rect, model):
        SceneBase.__init__(self)

        self.model = model

        self.rect = screen_rect
        self.surface = pygame.Surface(self.rect.size)

        world_rect = pygame.rect.Rect((0, 0), (self.rect.h, self.rect.h))
        self.world_surface = self.surface.subsurface(world_rect)
        self.world_scene = WorldScene(self.model)

        info_rect = ((world_rect.w, 0), (self.rect.w - world_rect.w, self.rect.h))
        self.info_surface = self.surface.subsurface(info_rect)
        self.info_scene = InfoScene(self.world_scene, self.model)

    def process_input(self, events, key_pressed):

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.switch_to_scene(main_scene.MainScene(self.rect, self.model))
                return

        self.world_scene.process_input(events, key_pressed)
        self.info_scene.process_input(events, key_pressed)

    def compute(self):
        self.world_scene.compute()
        self.info_scene.compute()

    def render(self, surface):
        self.world_scene.render(self.world_surface)
        self.info_scene.render(self.info_surface)

        surface.blit(self.surface, (0,0))