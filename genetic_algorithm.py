import random

from deap import base
from deap import creator
from deap import tools

import parameters


creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)


class GeneticAlgorithm:

    def __init__(self, creatures):
        self.creatures = creatures
        self.toolbox = base.Toolbox()

        self.toolbox.register("attr_float", random.uniform, -1.0, 1.0)

        chromo_length = self.creatures[0].nn.weights.size
        chromo_length += self.creatures[0].nn.bias.size
        self.toolbox.register("individual", tools.initRepeat, creator.Individual,
                              self.toolbox.attr_float, chromo_length)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)

        # Operator registration
        # self.toolbox.register("evaluate", self.eval_creature)
        self.toolbox.register("mate", tools.cxTwoPoint)
        self.toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
        self.toolbox.register("select", tools.selTournament, tournsize=3)

        self.pop = self.toolbox.population(n=parameters.N_POPULATION)

        for c, g in zip(self.creatures, self.pop):
            c.nn.set_parameters(g)

        self.generation = 1

    def compute(self):
        for ind, c in zip(self.pop, self.creatures):
            ind.fitness.values = c.food,

        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in self.pop]

        length = len(self.pop)
        mean = sum(fits) / length
        sum2 = sum(x * x for x in fits)
        std = abs(sum2 / length - mean ** 2) ** 0.5

        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)

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
        for c in self.creatures:
            c.food = 0

        # The population is entirely replaced by the offspring
        self.pop[:] = offspring

        for c, g in zip(self.creatures, self.pop):
            c.nn.set_parameters(g)