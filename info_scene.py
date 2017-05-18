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
        self.simu_model = model.simulation

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
        label = self.font.render("Simulation Time: {:2.1f}s".format(self.simu_model.simulation_time_ms / 1000), 1, InfoScene.COLOR_FONT)
        surface.blit(label, (10, line))

        # 3
        line += InfoScene.LINE_STEP
        label = self.font.render("Generation: {}".format(self.simu_model.gen_algo.generation), 1, InfoScene.COLOR_FONT)
        surface.blit(label, (10, line))

        # 4
        line += InfoScene.LINE_STEP
        ga = self.simu_model.gen_algo
        label = self.font.render("min:{} max:{} avg:{:2.1f} std:{:2.1f}".format(ga.min, ga.max, ga.mean, ga.std), 1, InfoScene.COLOR_FONT)
        surface.blit(label, (10, line))

        # Creature
        creature = self.world.creature_selected if self.world.creature_selected else self.world.best

        if creature:
            line += InfoScene.LINE_STEP
            label = self.font.render("Radius:{} Force:{} Mass:{}".format(creature.radius, creature.force, creature.mass)
                                     , 1, InfoScene.COLOR_FONT)
            surface.blit(label, (10, line))

            # Inputs
            line += InfoScene.LINE_STEP
            label = self.font.render("Inputs:", 1, InfoScene.COLOR_FONT)
            surface.blit(label, (10, line))

            text = [u"{0:0.2f}".format(i) for i in creature.nn.inputs.tolist()[0]]
            for t in text:
                label = self.font.render(t, 1, InfoScene.COLOR_FONT)
                line += InfoScene.LINE_STEP
                surface.blit(label, (10, line))

            # Outputs
            line += InfoScene.LINE_STEP
            label = self.font.render("Outputs:", 1, InfoScene.COLOR_FONT)
            surface.blit(label, (10, line))

            text = [u"{0:0.2f}".format(i) for i in creature.nn.outputs.tolist()[0]]
            for t in text:
                label = self.font.render(t, 1, InfoScene.COLOR_FONT)
                line += InfoScene.LINE_STEP
                surface.blit(label, (10, line))

            line += InfoScene.LINE_STEP
            label = self.font.render("Calories: {}".format(creature.food), 1, InfoScene.COLOR_FONT)
            surface.blit(label, (10, line))
