import pygame

from scene_base import SceneBase
from color import *


class InfoScene(SceneBase):

    def __init__(self, world, clock):
        self.font = pygame.font.SysFont("monospace", 15)
        self.world = world
        self.clock = clock

    def process_input(self, events, key_pressed):
        pass

    def compute(self):
        pass

    def render(self, surface):
        surface.fill(LIGHT_BLUE)

        zoom_label = self.font.render("Zoom: {:2.2f}".format(self.world.camera.zoom), 1, BLACK)
        surface.blit(zoom_label, (10, 10))

        zoom_label = self.font.render("FPS: {:2.1f}".format(self.clock.get_fps()), 1, BLACK)
        surface.blit(zoom_label, (150, 10))

        # Creature
        creature = self.world.creature_selected
        if creature:
            zoom_label = self.font.render("Power: {:2.2f}/{:2.2f}".format(creature.left_power, creature.right_power), 1, BLACK)
            surface.blit(zoom_label, (10, 30))

            zoom_label = self.font.render("Inputs: {}".format(creature.nn.inputs), 1, BLACK)
            surface.blit(zoom_label, (10, 50))

            zoom_label = self.font.render("Outputs: {}".format(creature.nn.outputs), 1, BLACK)
            surface.blit(zoom_label, (10, 70))

            zoom_label = self.font.render("Calories: {}".format(creature.calorie), 1, BLACK)
            surface.blit(zoom_label, (10, 90))
