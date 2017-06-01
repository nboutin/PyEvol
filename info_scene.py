import pygame
import datetime

import color


class InfoScene:

    ANTIALIAS = 1

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

    def __blit(self, text):
        return self.font.render(text, InfoScene.ANTIALIAS, InfoScene.COLOR_FONT)

    def header(self, surface, pos):
        text = "FPS:{:2.1f} Total Time:{!s:0>8}".format(self.model.clock.get_fps(),
                                                        datetime.timedelta(milliseconds=self.model.total_time_ms))
        surface.blit(self.__blit(text), pos)
        pos.y += 20

    def simulation(self, surface, pos):
        ga = self.simu_model.gen_algo

        text = "Generation:{} Simulation Time:{:2.1f}s".format(ga.generation,
                                                                self.simu_model.simulation_time_ms / 1000)
        surface.blit(self.__blit(text), pos)
        pos.y += 20

        text = "Min:{} Max:{} Avg:{:2.1f} Std:{:2.1f}".format(ga.min, ga.max, ga.mean, ga.std)
        surface.blit(self.__blit(text), pos)
        pos.y += 20

    def creature(self, surface, pos, c):
        """c: creature"""

        try:
            p = [u"{0:0.0f}".format(i) for i in c.body.position]
            text = "({}, {}) Radius:{} Force:{} Mass:{}".format(p[0], p[1], c.radius, c.force, c.mass)

            surface.blit(self.__blit(text), pos)
            pos.y += 20

            # Inputs
            line = pos.y
            surface.blit(self.__blit("Inputs"), pos)
            pos.y += 20
            self.__blit_list(surface, pos, c.nn.inputs.tolist()[0])
            pos.y += 20

            # Outputs
            pos.y = line
            pos.x += 70
            surface.blit(self.__blit("Outputs"), pos)
            pos.y += 20
            self.__blit_list(surface, pos, c.nn.outputs.tolist()[0])
            pos.y += 20

            # Calories
            pos.y = line
            pos.x += 80
            text = "Calories:{}".format(c.food)
            surface.blit(self.__blit(text), pos)

        except AttributeError:
            pass

    def __blit_list(self, surface, pos, l):
        text = [u"{0:0.2f}".format(i) for i in l]
        print(text)
        for t in text:
            surface.blit(self.__blit(t), pos)
            pos.y += 20

    def render(self, surface):

        surface.fill(color.PLUM)

        pos = pygame.rect.Rect((10, 10), (1,1))

        self.header(surface, pos)

        pos.y += 20
        self.simulation(surface, pos)

        pos.y += 20
        creature = self.world.creature_selected if self.world.creature_selected else self.world.best
        self.creature(surface, pos, creature)
