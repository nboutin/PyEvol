import unittest
import sys
import numpy as np

sys.path.insert(0, '..')
from neural_network import NeuralNetwork 


class NeuralNetworkTest(unittest.TestCase):

    def test_size(self):
        self.assertEqual(NeuralNetwork.size(2, [2]), 6)
        self.assertEqual(NeuralNetwork.size(2, [4, 2]), 22)

    def test_set_parameters2(self):
        nn_param = (1, 2, 3, 4, 5, 6, 7, 8, 1, 1)
        nn = NeuralNetwork(4, [2], nn_param)

        r_w = np.matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
        r_b = np.matrix([1, 1])

        self.assertListEqual(nn._NeuralNetwork__w[0].flatten().tolist(), r_w.flatten().tolist())
        self.assertListEqual(nn._NeuralNetwork__b[0].flatten().tolist(), r_b.flatten().tolist())

    def test_set_parameters(self):
        nn_param = (2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5)
        nn = NeuralNetwork(2, [4, 2], nn_param)

        r_w0 = np.matrix([[2, 2, 2, 2], [2, 2, 2, 2]])
        r_b0 = np.matrix([3, 3, 3, 3])
        r_w1 = np.matrix([[4, 4], [4, 4], [4, 4], [4, 4]])
        r_b1 = np.matrix([5, 5])

        self.assertListEqual(nn._NeuralNetwork__w[0].flatten().tolist(), r_w0.flatten().tolist())
        self.assertListEqual(nn._NeuralNetwork__b[0].flatten().tolist(), r_b0.flatten().tolist())
        self.assertListEqual(nn._NeuralNetwork__w[1].flatten().tolist(), r_w1.flatten().tolist())
        self.assertListEqual(nn._NeuralNetwork__b[1].flatten().tolist(), r_b1.flatten().tolist())

    
    def test_compute1(self):

        nn_param = (1, 2, 3, 4, 5, 6, 7, 8, 1, 1)
        nn = NeuralNetwork(4, [2], nn_param)
        result = [1.0, 1.0]

        input = np.matrix([1, 1, 1, 1])
        output = nn.compute(input)

        for o, r in zip(output, result):
            self.assertAlmostEqual(o, r)

    def test_compute2(self):

        nn_param = (1, 2, 3, 4, 5, 6, 7, 8, 1, 1)
        nn = NeuralNetwork(4, [2], nn_param)
        nn.activation = None
        result = [17, 21]

        input = np.matrix([1, 1, 1, 1])
        output = nn.compute(input)

        self.assertListEqual(output, result)

    def test_compute3(self):

        nn_param = (5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
        nn = NeuralNetwork(4, [2], nn_param)
        nn.activation = None
        result = [103, 114]

        input = np.matrix([1, 2, 3, 4])
        output = nn.compute(input)

        self.assertListEqual(output.tolist()[0], result)

    def test_compute3(self):

        nn_param = (2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5)
        nn = NeuralNetwork(2, [4, 2], nn_param)
        nn.activation = None
        result = [117, 117]

        input = np.matrix([1, 1])
        output = nn.compute(input)

        self.assertListEqual(output, result)

if __name__ == '__main__':
    unittest.main()
