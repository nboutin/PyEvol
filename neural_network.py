import numpy as np
from scipy.special import expit


class NeuralNetwork:

    # HIDDEN_NEURON_COUNT = 8

    def __init__(self, input_count, output_count):

        self.input_count = input_count
        self.output_count = output_count

        self.weights = np.zeros(shape=(input_count, output_count))
        self.bias = np.zeros(shape=(1, output_count))

        # self.weights = np.matrix(np.random.uniform(low=-1.0, size=(input_count, output_count)), dtype=float)
        # self.bias = np.matrix(np.random.uniform(low=-1.0, size=(1, output_count)), dtype=float)

        self.inputs = ()
        self.outputs = ()

    def set_parameters(self, param):
        self.weights = np.matrix([param[0:2], param[2:4]])
        self.bias = np.matrix([param[4:6]])

    def compute(self, inputs):
        self.inputs = inputs
        self.outputs = expit(np.matmul(inputs, self.weights) + self.bias).tolist()[0]
        return self.outputs
