import itertools
import math
from copy import deepcopy
from random import choice, random, randint, sample


class ant:
    def __init__(self, n, m):
        self.line = 0
        self.matrix=0

        self.all_perm = list(itertools.permutations([item for item in range(1, n + 1)]))
        self.size =len(self.all_perm)

        self.l1 = sample(list(itertools.permutations([item for item in range(1, n + 1)])), n)
        self.l2 = sample(
            [x for x in list(itertools.permutations([item for item in range(1, n + 1)])) if x not in self.l1], n)
        self.l = [self.l1, self.l2]
        self.path = [deepcopy(self.l)]
        self.n = n
        self.m = m

    def getMatrix(self):
        return self.matrix
    def getLine(self):
        return self.line

    def nextMoves(self, a):
        # returneaza o lista de posibile mutari corecte de la pozitia a
        new = []
        self.line = randint(0, self.n - 1)
        self.matrix = randint(0, 1)
        all_perm = self.all_perm
        newMatrix = deepcopy(self.l)
        for i in range(math.factorial(self.n)):
            if all_perm[i] not in newMatrix[self.matrix]:
                newMatrix[self.matrix][self.line] = all_perm[i]
                dummy = ant(self.n, self.m)
                dummy.l=newMatrix
                if newMatrix not in self.path and self.fitness()>dummy.fitness():
                    new.append(deepcopy(newMatrix))
        return new.copy()


    def distMove(self, a):
        # returneaza o distanta empirica data de numarul de posibile mutari corecte
        # dupa ce se adauga pasul a in path
        dummy = ant(self.n, self.m)
        dummy.path = self.path.copy()
        dummy.l=deepcopy(self.l)
        dummy.l[self.matrix][self.line]= a
        dummy.path.append(dummy.l)
        return dummy.fitness()

    def addMove(self, q0, trace, alpha, beta):
        # adauga o noua pozitie in solutia furnicii daca este posibil
        p={}
        for i in range (len(self.all_perm)):
            p[self.all_perm[i]]=0
        nextSteps = deepcopy(self.nextMoves(self.l))
        if (len(nextSteps) == 0):
            return False
        # punem pe pozitiile valide valoarea distantei empirice
        for i in self.all_perm:
            p[i] = self.distMove(i)
        # calculam produsul trace^alpha si vizibilitate^beta
        # matrix=matricea in care s-a facut modificarea-0 sau 1
        # line=linia in care s-a facut modificarea
        matrix=self.matrix
        line=self.line
        for i in self.all_perm:
            p[i]=(p[i] ** beta) * (trace[self.l[matrix][line]][i] ** alpha)
        if (random() < q0):
            for i in self.all_perm:
                p[i]=[i,p[i]]
            p = max(list(p.values()), key=lambda a: a[1])
            dummy = ant(self.n, self.m)
            dummy.l = deepcopy(self.l)
            dummy.l[matrix][line] = p[0]
            if (dummy.fitness() > self.fitness()):
                self.l[matrix][line]=p[0]
                self.path.append(deepcopy(self.l))
        else:
            # adaugam cu o probabilitate un drum posibil (ruleta)
            s = sum(p.values())
            if (s == 0):
                return choice(nextSteps)
            for i in self.all_perm:
                p[i]=p[i] / s
            val=list(p.values())
            val = [sum(val[0:i + 1]) for i in range(len(val))]
            r = random()
            i = 0
            while (r > val[i]):
                i = i + 1
            dummy = ant(self.n, self.m)
            dummy.l = deepcopy(self.l)
            dummy.l[matrix][line] = list(p.items())[i][0]
            if(dummy.fitness()>self.fitness()):
                self.l[matrix][line]=list(p.items())[i][0]
                self.path.append(deepcopy(self.l))
        return True
    def f(self):
        return len(self.path)
    def fitness(self):

        individual0 = self.l1
        individual1 = self.l2
        n0 = len(individual0)
        n1 = len(individual1)

        trans0 = [[individual0[j][i] for j in range(n0)] for i in range(len(individual0[0]))]

        trans1 = [[individual1[j][i] for j in range(n1)] for i in range(len(individual1[0]))]
        f = 0;
        #check for lines and columns that are not permutations
        for i in range(n0):
            if sorted(individual0[i]) != [item for item in range(1, n0 + 1)]:
                f += 1
            if sorted(trans0[i]) != [item for item in range(1, n0 + 1)]:
                f += 1
            if sorted(individual1[i]) != [item for item in range(1, n1 + 1)]:
                f += 1
            if sorted(trans1[i]) != [item for item in range(1, n1 + 1)]:
                f += 1
        f *= 2  # 1->9|2->8|3->0,10,10,4,10|4->13,4,4,10|5->14,15 |,6->16
        #check for duplicated pairs
        arr = []
        for i in range(n0):
            for j in range(n0):
                arr.append((trans0[i][j], trans1[i][j]))
        index = 0
        for i in range(len(arr)):
            index += arr[(i + 1):].count(arr[i])
        if index > 0:
            f += index
        return f
    def __str__(self):
        return str(self.l)