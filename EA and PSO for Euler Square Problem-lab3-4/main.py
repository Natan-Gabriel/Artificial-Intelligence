# -*- coding: utf-8 -*-
import sys
from controller import Controller
from problem import Problem
import matplotlib.pyplot as plt
import numpy as np
from qtpy.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit, QInputDialog, \
    QLabel

class UI(QWidget):
    def __init__(self):
        self.__problem = Problem()
        self.__controller=Controller(self.__problem)
        super().__init__()
        #self.validation()

        self.initUI()

    def initUI(self):
        self.l0 = QLabel(self)
        self.l0.setText("1.EA;2.HC;3.PSO")
        self.l0.move(0, 210)

        self.le0 = QLineEdit(self)
        self.le0.move(150, 210)

        self.l1 = QLabel(self)
        self.l1.setText("Probability of mutation")
        self.l1.move(0,0)

        self.le1 = QLineEdit(self)
        self.le1.move(150, 0)
        #
        self.l2 = QLabel(self)
        self.l2.setText("Population size")
        self.l2.move(0, 30)

        self.le2 = QLineEdit(self)
        self.le2.move(150, 30)
        #
        self.l3 = QLabel(self)
        self.l3.setText("Number of iterations")
        self.l3.move(0, 60)

        self.le3 = QLineEdit(self)
        self.le3.move(150, 60)
        #
        self.l4 = QLabel(self)
        self.l4.setText("Number of neighbours")
        self.l4.move(0,90)

        self.le4 = QLineEdit(self)
        self.le4.move(150, 90)
        #
        self.l5 = QLabel(self)
        self.l5.setText("w")
        self.l5.move(0, 120)

        self.le5 = QLineEdit(self)
        self.le5.move(150, 120)
        #
        self.l6 = QLabel(self)
        self.l6.setText("c1")
        self.l6.move(0, 150)

        self.le6 = QLineEdit(self)
        self.le6.move(150, 150)
        #
        self.l7 = QLabel(self)
        self.l7.setText("c2")
        self.l7.move(0, 180)

        self.le7 = QLineEdit(self)
        self.le7.move(150, 180)

        self.qtable = QTableWidget(self)
        self.qtable.move(200, 300)
        self.qtable.setGeometry(200, 300,600,600)

        self.setWindowTitle('Input dialog')

        self.btn = QPushButton('Take arguments', self)
        self.btn.move(200, 250)
        self.btn.clicked.connect(self.showDialog)

        self.show()

    def showDialog(self):
        if isinstance(self.le1.text(), str) and self.le1.text()!='':
            pM=float(self.le1.text())
        else:
            pM=0
        if isinstance(self.le2.text(), str) and self.le2.text() != '':
            dimPopulation = int(self.le2.text())
        else:
            dimPopulation = 20
        if isinstance(self.le3.text(), str) and self.le3.text()!='':
            noIteratii=int(self.le3.text())
        else:
            noIteratii=1000
        if isinstance(self.le4.text(), str) and self.le4.text()!='':
            sizeOfNeighborhood=int(self.le4.text())
        else:
            sizeOfNeighborhood=2
        if isinstance(self.le5.text(), str) and self.le5.text()!='':
            w=float(self.le5.text())
        else:
            w=1
        if isinstance(self.le6.text(), str) and self.le6.text()!='':
            c1=float(self.le6.text())
        else:
            c1=1
        if isinstance(self.le7.text(), str) and self.le7.text()!='':
            c2=float(self.le7.text())
        else:
            c2=2.5

        if isinstance(self.le0.text(), str) and self.le0.text()!='':
            a=self.le0.text()
        else:
            a=0

        self.run(a,pM,dimPopulation,noIteratii,sizeOfNeighborhood,w,c1,c2)


    def printMatrix(self,array):
        self.qtable.setColumnCount(len(array[0]))  # rows and columns of table
        self.qtable.setRowCount(len(array[0]))
        for row in range(len(array[0])):  # add items from array to QTableWidget
            for column in range(len(array[0])):
                item = (array[0][row][column],array[1][row][column])  # each item is a QTableWidgetItem
                self.qtable.setItem(row, column, QTableWidgetItem(str(item)))

        self.qtable.show()

    def case1(self, a, pM, dimPopulation, noIteratii, sizeOfNeighborhood, w, c1, c2):
        dimIndividual=4
        P = self.__problem.population(dimPopulation, dimIndividual,0, 0)
        for i in range(noIteratii):
            P = self.__controller.iteration(P, pM, 0,0)

        # print the best individual
        graded = [(self.__problem.fitness(x), x) for x in P]
        graded = sorted(graded)
        result = graded[0]
        fitnessOptim = result[0]
        individualOptim = result[1]
        self.printMatrix(individualOptim)

    def case2(self, a, pM, dimPopulation, noIteratii, sizeOfNeighborhood, w, c1, c2):
        dimIndividual=4
        ind = self.__problem.individual(dimIndividual,0, 0)
        res = self.__controller.hillClimb(ind)
        self.printMatrix(res)
    def case3(self,a,pM,dimPopulation,noIteratii,sizeOfNeighborhood,w,c1,c2):
        noParticles = dimPopulation
        # individual size
        dimParticle = 4
        # the boundries of the search interval
        vmin = -100
        vmax = -10
        # specific parameters for PSO
        w = 1.0
        c1 = 1.
        c2 = 2.5
        # sizeOfNeighborhood = 2
        P = self.__problem.populationForParticles(noParticles, dimParticle, vmin, vmax)
        # we establish the particles' neighbors
        neighborhoods = self.__problem.selectNeighbors(P, sizeOfNeighborhood)

        for i in range(noIteratii):
            P = self.__controller.iterationForParticles(P, neighborhoods, c1, c2, w / (i + 1))

        # print the best individual
        best = 0
        for i in range(1, len(P)):
            if (P[i].fitness < P[best].fitness):
                best = i

        fitnessOptim = P[best].fitness
        individualOptim = P[best].pozition
        self.printMatrix(individualOptim)


    def run(self,a,pM,dimPopulation,noIteratii,sizeOfNeighborhood,w,c1,c2):#ui
        dimIndividual = 4
        vmin = 0
        vmax = 0
        if a=="1":
            self.case1(a, pM, dimPopulation, noIteratii, sizeOfNeighborhood, w, c1, c2)
        if a=="2":
            self.case2(a,pM,dimPopulation,noIteratii,sizeOfNeighborhood,w,c1,c2)
        if a=="3":
            self.case3(a,pM,dimPopulation,noIteratii,sizeOfNeighborhood,w,c1,c2)

    def validation(self):
        fitnessOptimForEA=[]
        for i in range(30):
            dimIndividual=4
            dimPopulation=40
            noIteratii=1000
            pM=0.01
            P = self.__problem.population(dimPopulation, dimIndividual, 0,0)

            for i in range(noIteratii):
                P = self.__controller.iteration(P, pM, 0, 0)

            graded = [(self.__problem.fitness(x), x) for x in P]
            graded = sorted(graded)
            result = graded[0]
            fitnessOptimForEA.append(result[0])

        fitnessOptimForHC = []
        for i in range(30):
            dimIndividual=4
            ind = self.__problem.individual(dimIndividual,0, 0)
            res = self.__controller.hillClimb(ind)
            fitnessOptimForHC.append(self.__problem.fitness(res))

        fitnessOptimForPSO = []
        for i in range(3):
            noIteratii = 1000
            noParticles = 40
            dimParticle = 4
            # the boundries of the search interval
            vmin = -100
            vmax = -10
            # specific parameters for PSO
            w = 1.0
            c1 = 1.
            c2 = 2.5
            sizeOfNeighborhood = 2
            P = self.__problem.populationForParticles(noParticles, dimParticle, vmin, vmax)
            neighborhoods = self.__problem.selectNeighbors(P, sizeOfNeighborhood)
            for i in range(noIteratii):
                P = self.__controller.iterationForParticles(P, neighborhoods, c1, c2, w / (i + 1))
            best = 0
            for i in range(1, len(P)):
                if (P[i].fitness < P[best].fitness):
                    best = i
            fitnessOptim = P[best].fitness
            fitnessOptimForPSO.append(fitnessOptim)


        plt.plot(fitnessOptimForEA)  # plotting by columns
        np1 = np.array(fitnessOptimForEA)
        std1 = np.std(np1)
        m1 = np.mean(np1)
        plt.xlabel("standard deviation= " + str(std1) + ";mean= " + str(m1)+"            Trials")
        plt.ylabel("EA algorithm"+"              Fitness")
        plt.show()

        plt.plot(fitnessOptimForHC)  # plotting by columns
        np2 = np.array(fitnessOptimForHC)
        std2 = np.std(np2)
        m2 = np.mean(np2)
        plt.xlabel("standard deviation= " + str(std2) + ";mean= " + str(m2)+"            Trials")
        plt.ylabel("HC algorithm"+"              Fitness")
        plt.show()

        plt.plot(fitnessOptimForPSO)  # plotting by columns
        np3 = np.array(fitnessOptimForPSO)
        std3 = np.std(np3)
        m3 = np.mean(np3)
        plt.xlabel("standard deviation= " + str(std3) + ";mean= " + str(m3)+"            Trials")
        plt.ylabel("PSO algorithm"+"              Fitness")
        plt.show()





def main():
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())
main()

