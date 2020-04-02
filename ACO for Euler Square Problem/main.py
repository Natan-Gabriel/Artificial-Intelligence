import itertools
import matplotlib.pyplot as plt
import numpy as np

from Problem import Problem
from controller import controller


class UI:
    def printMatrix(self,m):
        arr=[]
        for i in range(len(m[0])):
            arr = []
            for j in range(len(m[0])):
                arr.append((m[0][i][j], m[1][i][j]))
            print(arr)

    def main(self,n=4, noEpoch=100, noAnts=3, alpha=1.9, beta=0.9, rho=0.05, q0=0.5):
        ctrl=controller()
        pr=Problem(ctrl)


        while True:
            #try:
                sol = []
                bestSol = []

                a=input("Input 1 if you want to change the parameters?")
                if a=="1":
                    n=int(input("n="))
                    noEpoch=int(input("noEpoch="))
                    noAnts=int(input("noAnt="))
                    alpha=float(input("alpha="))
                    beta=float(input("beta="))
                    rho=float(input("rho="))
                    q0=float(input("q0="))

                trace = {}
                for i in list(itertools.permutations([item for item in range(1, n + 1)])):
                    trace[i] = {}
                    for j in list(itertools.permutations([item for item in range(1, n + 1)])):
                        trace[i][j] = {}
                        trace[i][j] = 1

                print("Programul ruleaza! Dureaza ceva timp pana va termina!")

                for i in range(noEpoch):
                    sol = ctrl.epoca(n,n,noAnts, trace,alpha, beta, q0, rho).copy()
                    if pr.fitness(sol) < pr.fitness(bestSol):
                        bestSol = sol.copy()
                        print("Best sol UNTIL NOW:")
                        self.printMatrix(bestSol)
                        print("Fitness for best sol UNTIL NOW:", pr.fitness(bestSol))

                print("Best sol:")
                self.printMatrix(bestSol)
                print("Fitness for best sol is", pr.fitness(bestSol))




    def validation(self):
        fitnessOptimForACO=[]
        for i in range(30):
            n=4
            noEpoch=10
            noAnts=3
            alpha=1.9
            beta=0.9
            rho=0.05
            q0=0.5
            ctrl = controller()
            pr = Problem(ctrl)
            sol = []
            bestSol = []
            trace = {}
            for i in list(itertools.permutations([item for item in range(1, n + 1)])):
                trace[i] = {}
                for j in list(itertools.permutations([item for item in range(1, n + 1)])):
                    trace[i][j] = {}
                    trace[i][j] = 1


            for i in range(noEpoch):
                sol = ctrl.epoca(n,n, noAnts, trace, alpha, beta, q0, rho).copy()
                if pr.fitness(sol) < pr.fitness(bestSol):
                    bestSol = sol.copy()

            fitnessOptimForACO.append(pr.fitness(bestSol))


        plt.plot(fitnessOptimForACO)  # plotting by columns
        np1 = np.array(fitnessOptimForACO)
        std1 = np.std(np1)
        m1 = np.mean(np1)
        plt.xlabel("standard deviation= " + str(std1) + ";mean= " + str(m1)+"            Trials")
        plt.ylabel("ACO algorithm"+"              Fitness")
        plt.show()




ui=UI()
#ui.validation()
ui.main()
