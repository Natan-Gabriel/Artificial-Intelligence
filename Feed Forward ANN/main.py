'''
An example of a simple ANN with 1+2 layers
The implementation uses 2 matrixes in order to memorise the weights.


For a full description:

https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6

'''
from copy import deepcopy
from random import shuffle
import numpy as np
import matplotlib.pyplot as pyplot
from Repository import Repository
from controller import NeuralNetwork
np.set_printoptions(precision=4,threshold=10000,linewidth=150,suppress=True)

class UI:
    def __init__(self):
        self.repo=Repository("data.txt")

    def run(self):
        # X the array of inputs, y the array of outputs, 4 pairs in total
        print(self.repo.input)
        print(self.repo.output)

        x = np.array(self.repo.input)
        y = np.array(self.repo.output)


        nn = NeuralNetwork(x, y, 5)

        nn.loss = []
        iterations = []
        for i in range(100000):
            nn.feedforward()
            nn.backprop(0.0000001)
            iterations.append(i)

        print(nn.output)
        print(nn.computeLoss(y,nn.output))
        pyplot.plot(iterations[50:], nn.loss[50:], label='loss value vs iteration')
        pyplot.xlabel('Iterations')
        pyplot.ylabel('loss function')
        pyplot.legend()
        pyplot.show()
#import tensorflow as tf
#tf.config.optimizer.set_jit(True
import tensorflow as tf
tf.config.optimizer.set_jit(True)

ui=UI()
ui.run()