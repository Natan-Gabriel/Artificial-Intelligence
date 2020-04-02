import itertools
from copy import deepcopy
from random import randint


class Controller:
    def __init__(self,problem):
        self.__problem=problem
    def iteration(self,pop, pM, vmin, vmax):

        i1 = randint(0, len(pop) - 1)
        i2 = randint(0, len(pop) - 1)
        if (i1 != i2):
            c = self.__problem.crossover(pop[i1], pop[i2])
            c = self.__problem.mutate(c, pM, vmin, vmax)
            f1 = self.__problem.fitness(pop[i1])
            f2 = self.__problem.fitness(pop[i2])

            fc = self.__problem.fitness(c)
            if (f1 > f2) and (f1 > fc):
                pop[i1] = c
            if (f2 > f1) and (f2 > fc):
                pop[i2] = c
        return pop


    def hillClimb(self,s):
        x = deepcopy(s)
        k = 0
        while self.__problem.fitness(x)!=0:
            k = k + 1
            p=randint(0,len(s[0])-1)
            p1=randint(0,1)
            x1 = deepcopy(x)
            for i in list(itertools.permutations([item for item in range(1, len(s[0])+1)])):
                x1[p1][p]=i
                if self.__problem.fitness(x1)<self.__problem.fitness(s):
                    s=deepcopy(x1) #s is best neighbour
            if self.__problem.fitness(s)<self.__problem.fitness(x):
                x=s
            else:
                return x
        return x


    def hillClimb1(self,s):
        x = deepcopy(s)
        k = 0
        while self.__problem.fitness(x)!=0:
            k = k + 1
            l1=randint(0,len(s[0])-1)
            l2 = randint(0, len(s[0]) - 1)
            p1=randint(0,1)
            x1 = deepcopy(x)
            for i in list(itertools.permutations([item for item in range(1, len(s[0])+1)])):
                x1[p1][l1] = i
                for j in list(itertools.permutations([item for item in range(1, len(s[0])+1)])):
                    x1[p1][l2]=j
                    if self.__problem.fitness(x1)<self.__problem.fitness(s):
                        s=deepcopy(x1) #s is best neighbour

            if self.__problem.fitness(s)<self.__problem.fitness(x):
                x=s
            else:
                return x
        return x

    def getDist(self,v1,v2):
        s=0
        for i in range (len(v1)):
            s+=abs(v1[i]-v2[i])
        return s

    def iterationForParticles(self,pop, neighbors, c1, c2, w):

        bestNeighbors = []
        # determine the best neighbor for each particle
        for i in range(len(pop)):
            bestNeighbors.append(neighbors[i][0])
            for j in range(1, len(neighbors[i])):
                if (pop[bestNeighbors[i]].fitness > pop[neighbors[i][j]].fitness):
                    bestNeighbors[i] = neighbors[i][j]

        # update the velocity for each particle
        for i in range(len(pop)):
            for j in range(len(pop[0].velocity[0])):
                for k in range(len(pop[0].velocity[0])):
                    newVelocity = w * pop[i].velocity[0][j][k]
                    newVelocity = newVelocity + c1 * randint(1,len(pop[0].velocity[0])) * (pop[bestNeighbors[i]].pozition[0][j][k] - pop[i].pozition[0][j][k])
                    newVelocity = newVelocity + c2 * randint(1,len(pop[0].velocity[0])) * (pop[i].bestPozition[0][j][k] - pop[i].pozition[0][j][k])
                    newVelocity=int(round(newVelocity))
                    newVelocity=newVelocity%len(pop[0].velocity[0])
                    pop[i].velocity[0][j][k] = newVelocity
        for i in range(len(pop)):
            for j in range(len(pop[0].velocity[0])):
                for k in range(len(pop[0].velocity[0])):
                    pop[i].pozition[0][j][k]=(pop[i].pozition[0][j][k] + pop[i].velocity[0][j][k])%len(pop[0].velocity[0])


        return pop