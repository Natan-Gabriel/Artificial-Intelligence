class Problem:
    def __init__(self,ctrl):
        self.ctrl=ctrl

    def fitness(self,l):

        if l==[]:
            return 100000

        individual0 = l[0]
        individual1 = l[1]
        n0 = len(individual0)
        n1 = len(individual1)

        trans0 = [[individual0[j][i] for j in range(n0)] for i in range(len(individual0[0]))]

        trans1 = [[individual1[j][i] for j in range(n1)] for i in range(len(individual1[0]))]
        f = 0;
        for i in range(n0):
            if sorted(individual0[i]) != [item for item in range(1, n0 + 1)]:
                f += 1
            if sorted(trans0[i]) != [item for item in range(1, n0 + 1)]:
                f += 1
            if sorted(individual1[i]) != [item for item in range(1, n1 + 1)]:
                f += 1
            if sorted(trans1[i]) != [item for item in range(1, n1 + 1)]:
                f += 1
        f *= 2
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


