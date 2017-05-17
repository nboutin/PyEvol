import pygame
import pymunk
import numpy as np
import enum

import parameters
from creature import Creature
from genetic_algorithm import GeneticAlgorithm


class Model:
    def __init__(self, clock):
        self.clock = clock
        self.total_time_ms = 0

        self.simulation = SimulationModel(self)


class SimulationModel:

    class State(enum.Enum):
        START = 0
        CONTINUE = 1
        STOP = 2
        EXIT = 3

    def __init__(self, model):
        # self.__model = model

        self.delta_time = 0
        self.simulation_time_ms = 0
        self.state = SimulationModel.State.START

        self.rect = pygame.rect.Rect(0, 0, 1050, 1050)

        # pymunk
        self.space = pymunk.Space()
        self.space.gravity = (0.0, 0.0)

        self.creatures = list()
        for i in range(0, parameters.N_POPULATION):
            self.creatures.append(Creature(self.space))

        self.ga = GeneticAlgorithm(self.creatures)

    # @property
    # def state(self):
    #     print("getter {}".format(self.__state))
    #     return self.__state
    #
    # @state.setter
    # def state(self, s):
    #     self.__state = s
    #     print ("setter {}".format(s))

    def construct(self):
        for c in self.creatures:
            c.set_pos((np.random.randint(0, self.rect.width), np.random.randint(0, self.rect.height)))

        self.ga.update_creatures()
