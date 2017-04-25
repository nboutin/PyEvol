import unittest
import sys
import numpy as np

sys.path.insert(0, '..')
from neural_network import NeuralNetwork 


class NeuralNetworkTest(unittest.TestCase):
    
    def test_compute(self):
        
        nn = NeuralNetwork(4,2)
        
        nn.weights = np.matrix([[1,2],[3,4],[5,6],[7,8]])
        nn.bias = np.matrix([1,1])

        input = np.matrix([1, 1, 1, 1])
        output = nn.compute(input)

        print (input)
        print (nn.weights)
        print (nn.bias)
        print (output)

if __name__ == '__main__':
    unittest.main()
