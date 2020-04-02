import itertools
from random import sample, randint, random

from particle import particle


class Problem:
    def individual(self,length, vmin, vmax):
        l1=sample(list(itertools.permutations([item for item in range(1, length + 1)])), length)
        l2=sample([x for x in list(itertools.permutations([item for item in range(1, length + 1)])) if x not in l1],length)
        return [l1,l2]

    def population(self,count, length, vmin, vmax):
        return [self.individual(length, vmin, vmax) for x in range(count)]


    def fitness(self,individual):

        individual0 = individual[0]
        individual1 = individual[1]
        n0 = len(individual0)
        n1 = len(individual1)

        trans0 = [[individual0[j][i] for j in range(n0)] for i in range(len(individual0[0]))]

        trans1 = [[individual1[j][i] for j in range(n1)] for i in range(len(individual1[0]))]
        f = 0;
        for i in range(n0):
            if sorted(individual0[i])!=[item for item in range(1, n0+1)]:
                f+=1
            if sorted(trans0[i])!=[item for item in range(1, n0+1)]:
                f+=1
            if sorted(individual1[i])!=[item for item in range(1, n1+1)]:
                f+=1
            if sorted(trans1[i])!=[item for item in range(1, n1+1)]:
                f+=1
        f*=2
        arr=[]
        for i in range(n0):
            for j in range(n0):
                arr.append((trans0[i][j],trans1[i][j]))
        index=0
        for i in range (len(arr)):
            index+=arr[(i+1):].count(arr[i])
        if index>0:
            f+=index
        return f


    def mutate(self,individual, pM, vmin, vmax):
        if pM > random():
            p = randint(0, len(individual) - 1)
            alpha=randint(0, 1)
            gen=sample(list(itertools.permutations([item for item in range(1, len(individual[0]) + 1)])), 1)[0]
            while (gen in individual[0]) or (gen in individual[1]):
                gen=sample(list(itertools.permutations([item for item in range(1, len(individual[0]) + 1)])), 1)[0]
            individual[alpha][p] = gen

        return individual

    def crossover(self,parent1, parent2):
        child0 = []
        child1 = []
        parent = []
        parent.append(parent1)
        parent.append(parent2)
        for x in range(len(parent1[0])):
            gen = parent[randint(0, 1)][randint(0, 1)][randint(0,len(parent1[0])-1)]
            while ((gen in child0) or (gen in child1)):
                gen = parent[randint(0, 1)][randint(0, 1)][randint(0,len(parent1[0])-1)]
            child0.append(gen)

            gen = parent[randint(0, 1)][randint(0, 1)][randint(0,len(parent1[0])-1)]
            while ((gen in child0) or (gen in child1)):
                gen = parent[randint(0, 1)][randint(0, 1)][randint(0,len(parent1[0])-1)]
            child1.append(gen)

        return [child0, child1]

    #PARTICLES

    def populationForParticles(self,count, l, vmin, vmax):
        return [particle(l, vmin, vmax) for x in range(count)]

    def selectNeighbors(self,pop, nSize):
        if (nSize > len(pop)):
            nSize = len(pop)
        # Attention if nSize==len(pop) this selection is not a propper one
        neighbors = []
        for i in range(len(pop)):
            localNeighbor = []
            for j in range(nSize):
                x = randint(0, len(pop) - 1)
                while (x in localNeighbor):
                    x = randint(0, len(pop) - 1)
                localNeighbor.append(x)
            neighbors.append(localNeighbor.copy())
        return neighbors

