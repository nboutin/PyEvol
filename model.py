import parameters
from creature import Creature
from genetic_algorithm import GeneticAlgorithm


class Model:
    def __init__(self, clock):
        self.clock = clock
        self.playtime = 0

        self.creatures = list()
        for i in range(0, parameters.N_POPULATION):
            self.creatures.append(Creature())

        self.ga = GeneticAlgorithm(self.creatures)
