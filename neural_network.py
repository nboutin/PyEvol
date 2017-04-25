import numpy as np
from scipy.special import expit


class NeuralNetwork:

    # HIDDEN_NEURON_COUNT = 8

    def __init__(self, input_count, output_count):
        self.weights = np.matrix(np.random.uniform(low=-1.0, size=(input_count, output_count)), dtype=float)
        self.bias = np.matrix(np.random.uniform(low=-1.0, size=(1, output_count)), dtype=float)

        self.inputs = ()
        self.outputs = ()

    def compute(self, inputs):
        self.inputs = inputs
        self.outputs = expit(np.matmul(inputs, self.weights) + self.bias).tolist()[0]
        return self.outputs

