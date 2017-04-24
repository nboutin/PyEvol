import pygame

from scene_base import SceneBase
from color import *


class WorldScene(SceneBase):

    def process_input(self, events, pressed_keys):
        pass

    def compute(self):
        pass

    def render(self, surface):
        surface.fill(GRAY)

    def terminate(self):
        pass
