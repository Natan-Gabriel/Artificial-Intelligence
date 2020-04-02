from random import randint


class particle:

    def __init__(self, l, vmin, vmax):
        self._pozition = self.individual(l, vmin, vmax)
        self.evaluate()
        vect1=[[0 for x in range(l)] for y in range(l)]
        vect2 = [[0 for x in range(l)] for y in range(l)]
        self.velocity = [vect1,vect2]

        # the memory of that particle
        self._bestPozition = self._pozition.copy()
        self._bestFitness = self._fitness

    def individual(self,length, vmin, vmax):
        x1=[[randint(1,length) for x in range(length)] for x in range(length)]
        x2 = [[randint(1, length) for x in range(length)] for x in range(length)]
        return [x1,x2]

    def fit(self):

        individual0 = self._pozition[0]
        individual1 = self._pozition[1]
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
    def evaluate(self):
        """ evaluates the particle """
        self._fitness = self.fit()

    @property
    def pozition(self):
        """ getter for pozition """
        return self._pozition

    @property
    def fitness(self):
        """ getter for fitness """
        return self._fitness

    @property
    def bestPozition(self):
        """ getter for best pozition """
        return self._bestPozition

    @property
    def bestFitness(self):
        """getter for best fitness """
        return self._bestFitness

    @pozition.setter
    def pozition(self, newPozition):
        self._pozition = newPozition.copy()
        # automatic evaluation of particle's fitness
        self.evaluate()
        # automatic update of particle's memory
        if (self._fitness < self._bestFitness):
            self._bestPozition = self._pozition
            self._bestFitness = self._fitness

    def __str__(self):
        return str(self._pozition)