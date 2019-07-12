'''
Created on 12 juil. 2019

@author: nboutin
'''

import os
import neat
from math import pow

inputs = ((False,False,False),(False,False,True),(False,True,False),(False,True,True),
                  (True,False,False),(True,False,True),(True,True,False),(True,True,True))

def majorityFunction(a,b,c):
    '''M(A,B,C)=AB+AC+BC'''
    return a and b or a and c or b and c

def eval_genomes(genomes, config):
#     for genome_id, genome in genomes:
#             genome.fitness = 4.0
#             net = neat.nn.FeedForwardNetwork.create(genome, config)
#             for xi, xo in zip(xor_inputs, xor_outputs):
#                 output = net.activate(xi)
#                 genome.fitness -= (output[0] - xo[0]) ** 2
    for genome_id, genome in genomes:
        genome.fitness = float(len(inputs))
        net = neat.nn.FeedForwardNetwork.create(genome, config)
         
        for i in inputs:
            i_float = [float(x) for x in i] # from bool to float
            r = net.activate(i_float)
            
            a,b,c = i
            genome.fitness -= pow(r[0] - majorityFunction(a, b, c), 2)
            
def run(config_file):

    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'majority_config')
    run(config_path)