import random

from deap import base
from deap import creator
from deap import tools

import parameters


creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)


class GeneticAlgorithm:

    def __init__(self, world):
        self.world = world
        self.toolbox = base.Toolbox()

        self.toolbox.register("attr_float", random.uniform, -1.0, 1.0)

        chromo_length = self.world.creatures[0].nn.weights.size
        chromo_length += self.world.creatures[0].nn.bias.size
        self.toolbox.register("individual", tools.initRepeat, creator.Individual,
                              self.toolbox.attr_float, chromo_length)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)

        # Operator registration
        self.toolbox.register("evaluate", self.eval_creature)
        self.toolbox.register("mate", tools.cxTwoPoint)
        self.toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
        self.toolbax.register("select", tools.selTournament, tournsize=3)

        self.pop = self.toolbox.population(n=parameters.N_POPULATION)

    def eval_creature(self):
        pass