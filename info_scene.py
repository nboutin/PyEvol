import pygame

from scene_base import SceneBase
from color import *


class InfoScene(SceneBase):

    def __init__(self):
        self.font = pygame.font.SysFont("monospace", 15)

    def process_input(self, events, pressed_keys):
        pass

    def compute(self):
        pass

    def render(self, surface):
        surface.fill(LIGHT_BLUE)
        zoom_label = self.font.render("Zoom: 10", 1, BLACK)
        surface.blit(zoom_label, (10, 10))

    def terminate(self):
        pass
