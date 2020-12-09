from random import randint
from numpy.random.mtrand import choice
from math import sin, cos
from copy import deepcopy

from node import Node

DEPTH_MAX = 11


class Chromosome():
    def __init__(self, d=DEPTH_MAX):
        self.maxDepth = d
        self.fitness = 0
        self.root = Node()
        self.root.init(d)

    def evaluate(self, inputTrain, outputTrain):
        self.fitness = 0
        exp = str(self.root)
        for (x, y) in zip(inputTrain, outputTrain):
            for i in range(len(x)):
                from gpalgorithm import HEADER
                #print(HEADER[i], x[i])
                exec("{} = {}".format(HEADER[i], x[i]))
            #print("exp",exp)
            res = eval(exp)
            # if int(round(res))!=int(y):
            #     #print("int(round(res))",int(round(res)))
            #     #print("int(y)",int(y))
            #     self.fitness+=1
            #print("abs(res - y)",abs(res - y))
            self.fitness += abs(res - y)
        self.fitness = self.fitness / len(inputTrain)
        return self.fitness

    #@staticmethod
    def crossover(ch1, ch2, probability_crossover):
        node1 = choice(ch1.root.getNodes())
        node2 = choice(ch2.root.getNodes())
        c = Chromosome()
        if ch1.root == node1:  # if we must change the whole tree
            c.root = node2.deepcopy()
        else:
            c.root = Node()
            c.root.change(ch1.root, node1, node2)
        return c

    def mutate(self, prob):
        pos = randint(1, self.root.size)
        self.root.mutate(pos, prob)