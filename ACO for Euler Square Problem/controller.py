import itertools

from ant import ant


class controller:
    def __init__(self):
        self.antSet = []

    def epoca(self,noAnts, n, m, trace, alpha, beta, q0, rho):
        self.antSet = [ant(n, m) for i in range(noAnts)]
        all_perm = list(itertools.permutations([item for item in range(1, n + 1)]))
        size = len(all_perm)
        for i in range(size):
            # numarul maxim de iteratii intr-o epoca este lungimea solutiei
            for x in self.antSet:
                x.addMove(q0, trace, alpha, beta)

        dTrace = [1.0 / self.antSet[i].fitness() for i in range(len(self.antSet))]
        for i in all_perm:
            for j in all_perm:
                trace[i][j] = (1 - rho) * trace[i][j]

        for i in range(len(self.antSet)):
            for j in range(len(self.antSet[i].path) - 1):
                x = self.antSet[i].path[j]
                y = self.antSet[i].path[j + 1]
                res = self.getMatrixAndLine(x, y)
                mat = res[0]
                line = res[1]
                trace[mat][line] = trace[mat][line] + dTrace[i]

        # return best ant path
        f = [[self.antSet[i].fitness(), i] for i in range(len(self.antSet))]
        f = min(f)
        return self.antSet[f[1]].l
    def setTrace(self,trace):
        self.trace=trace

    def setAntSet(self, antSet):
        self.antSet = antSet

    def getMatrixAndLine(self,l1, l2):
        i = 0
        for i in range(len(l1[0])):
            if (l1[0][i] != l2[0][i]):
                return [l1[0][i], l2[0][i]]
        i = 0
        for i in range(len(l1[1])):
            if (l1[1][i] != l2[1][i]):
                return [l1[1][i], l2[1][i]]
        return [l1[0][i], l2[0][i]]
