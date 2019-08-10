import numpy as np
from scipy.special import expit


class NeuralNetwork:

    def __init__(self, input_count, hidden_layers, nn_param):
        """Create a new Neural Network
        
        :param input_count: number of input variables
        :param hidden_layers: list of layer size, last one is the output
        :param nn_param: 
        """

        self.input_count = input_count
        self.h_layers = hidden_layers

        self.activation = expit

        self.__w = list()
        self.__b = list()
        self.__set_parameters(nn_param)

        self.inputs = ()
        self.outputs = ()

    @staticmethod
    def size(n_in, layers):
        tmp_in = n_in
        result = 0

        for l in layers:
            result += tmp_in * l + l
            tmp_in = l

        return result

    def __set_parameters(self, param):
        n_in = self.input_count

        for l in self.h_layers:
            n_out = l
            self.__w.append(np.matrix(param[0:n_in * n_out]).reshape(n_in, n_out))
            param = param[n_in*n_out:]
            self.__b.append(np.matrix(param[0:n_out]).reshape(1, n_out))
            param = param[n_out:]
            n_in = l

    def compute(self, inputs):
        self.inputs = inputs
        m = inputs

        for w, b in zip(self.__w, self.__b):
            try:
                m = self.activation(np.matmul(m, w) + b)
            except TypeError:
                m = np.matmul(m, w) + b

        self.outputs = m
        return self.outputs.tolist()[0]
