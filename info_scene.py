import pygame
import datetime

import color
from scene_base import SceneBase


class InfoScene(SceneBase):

    LINE_STEP = 20
    COLOR_FONT = color.BLACK

    def __init__(self, world, model):
        self.font = pygame.font.SysFont("monospace", 15)
        self.world = world
        self.model = model

    def process_input(self, events, key_pressed):
        pass

    def compute(self):
        pass

    def render(self, surface):
        surface.fill(color.PLUM)

        line = 10
        label = self.font.render("Zoom: {:2.2f}".format(self.world.camera.zoom), 1, InfoScene.COLOR_FONT)
        surface.blit(label, (10, line))

        label = self.font.render("FPS: {:2.1f}".format(self.model.clock.get_fps()), 1, InfoScene.COLOR_FONT)
        surface.blit(label, (130, line))

        label = self.font.render("Total Time: {!s:0>8}".format(datetime.timedelta(milliseconds=self.model.total_time_ms)), 1, InfoScene.COLOR_FONT)
        surface.blit(label, (230, line))

        # 2
        line += InfoScene.LINE_STEP
        label = self.font.render("Simulation Time: {:2.1f}s".format(self.model.simulation_time_ms / 1000), 1, InfoScene.COLOR_FONT)
        surface.blit(label, (10, line))

        # 3
        line += InfoScene.LINE_STEP
        label = self.font.render("Generation: {}".format(self.model.ga.generation), 1, InfoScene.COLOR_FONT)
        surface.blit(label, (10, line))

        # 4
        line += InfoScene.LINE_STEP
        ga = self.model.ga
        label = self.font.render("min:{} max:{} avg:{:2.1f} std:{:2.1f}".format(ga.min, ga.max, ga.mean, ga.std), 1, InfoScene.COLOR_FONT)
        surface.blit(label, (10, line))


        # Creature
        creature = self.world.creature_selected
        if creature:
            line += InfoScene.LINE_STEP
            label = self.font.render("Power: {:2.2f}/{:2.2f}".format(creature.left_power, creature.right_power), 1, InfoScene.COLOR_FONT)
            surface.blit(label, (10, line))

            line += InfoScene.LINE_STEP
            label = self.font.render("Inputs: {}".format(creature.nn.inputs), 1, InfoScene.COLOR_FONT)
            surface.blit(label, (10, line))

            line += InfoScene.LINE_STEP
            label = self.font.render("Outputs: {}".format(creature.nn.outputs), 1, InfoScene.COLOR_FONT)
            surface.blit(label, (10, line))

            line += InfoScene.LINE_STEP
            label = self.font.render("Calories: {}".format(creature.food), 1, InfoScene.COLOR_FONT)
            surface.blit(label, (10, line))
