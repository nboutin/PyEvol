import random

from deap import base
from deap import creator
from deap import tools

import parameters


creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)


class GeneticAlgorithm:

    def __init__(self, gene_size):
        self.toolbox = base.Toolbox()

        self.toolbox.register("attr_float", random.uniform, -1.0, 1.0)

        self.toolbox.register("individual", tools.initRepeat, creator.Individual, self.toolbox.attr_float, gene_size)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)

        # Operator registration
        # self.toolbox.register("evaluate", self.eval_creature)
        self.toolbox.register("mate", tools.cxTwoPoint)
        self.toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
        self.toolbox.register("select", tools.selTournament, tournsize=3)

        self.pop = self.toolbox.population(n=parameters.N_POPULATION)

        self.generation = 1
        self.min = 0
        self.max = 0
        self.mean = 0
        self.std = 0

    def update_creatures(self, creatures):
        for c, g in zip(creatures, self.pop):
            c.nn.set_parameters(g)

    def compute(self, creatures):

        self.generation += 1

        for ind, c in zip(self.pop, creatures):
            ind.fitness.values = c.food,

        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in self.pop]

        length = len(self.pop)
        self.min = min(fits)
        self.max = max(fits)
        self.mean = sum(fits) / length
        sum2 = sum(x * x for x in fits)
        self.std = abs(sum2 / length - self.mean ** 2) ** 0.5

        # Select the next generation individuals
        offspring = self.toolbox.select(self.pop, len(self.pop))
        # Clone the selected individuals
        offspring = list(map(self.toolbox.clone, offspring))

        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):

            # cross two individuals with probability CXPB
            if random.random() < parameters.CXPB:
                self.toolbox.mate(child1, child2)

                # fitness values of the children
                # must be recalculated later
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            # mutate an individual with probability MUTPB
            if random.random() < parameters.MUTPB:
                self.toolbox.mutate(mutant)
                del mutant.fitness.values

        # Reset fitness (food)
        for c in creatures:
            c.food = 0

        # The population is entirely replaced by the offspring
        self.pop[:] = offspring

        self.update_creatures(creatures)