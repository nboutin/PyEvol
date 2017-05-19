import numpy as np
from scipy.special import expit


class NeuralNetwork:

    L1 = 4

    def __init__(self, input_count, output_count, nn_param):

        self.input_count = input_count
        self.output_count = output_count

        # 1
        # self.weights = np.zeros(shape=(input_count, output_count))
        # self.bias = np.zeros(shape=(1, output_count))

        # 2
        self.l1_weights = np.zeros(shape=(input_count, NeuralNetwork.L1))
        self.l1_bias = np.zeros(shape=(1, NeuralNetwork.L1))

        self.out_weights = np.zeros(shape=(NeuralNetwork.L1, output_count))
        self.out_bias = np.zeros(shape=(1, output_count))

        self.__set_parameters(nn_param)

        self.inputs = ()
        self.outputs = ()

    # @property
    # def size(self):
        # 1
        # return self.weights.size + self.bias.size

        # 2
        # return self.l1_weights.size + self.l1_bias.size + self.out_weights.size + self.out_bias.size

    def __set_parameters(self, param):
        n_in = self.input_count
        n_out = self.output_count

        #1
        # self.weights = np.matrix(param[0:n_in*n_out]).reshape(n_in,n_out)
        # param = param[0:n_in*n_out]
        # self.bias = np.matrix(param[0:n_out]).reshape(1, n_out)

        #2
        l1 = NeuralNetwork.L1
        n_in = self.input_count
        n_out = self.output_count

        self.l1_weights = np.matrix(param[0:2*l1]).reshape((n_in, l1))
        param = param[2*l1:]

        self.l1_bias = np.matrix(param[0:l1])
        param = param[l1:]

        self.out_weights = np.matrix(param[0:2*l1]).reshape((l1, n_out))
        param = param[2*l1:]

        self.out_bias = np.matrix(param[0: n_out]).reshape((1, n_out))

    def compute(self, inputs):

        self.inputs = inputs

        #1
        # self.outputs = expit(np.matmul(inputs, self.weights) + self.bias)
        # return self.outputs.tolist()[0]

        #2
        l1 = expit(np.matmul(inputs, self.l1_weights) + self.l1_bias)
        self.outputs = expit(np.matmul(l1, self.out_weights) + self.out_bias)
        return self.outputs.tolist()[0]
