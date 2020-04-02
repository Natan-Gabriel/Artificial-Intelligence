from time import time
import numpy as np


class Configuration:
    '''
    holds a configuration
    '''

    def __init__(self, positions):
        self.__size = len(positions)
        self.__values = positions[:]

    def getSize(self):
        return self.__size

    def getValues(self):
        return self.__values[:]

    def satisfyCond(self, i, j):
        for j1 in range(self.__size):
            if self.__values[i][j1] != 0:
                return False
        for i1 in range(self.__size):
            if self.__values[i1][j] != 0:
                return False
        i1 = i
        j1 = j
        while i1 >= 0 and j1 >= 0:
            if self.__values[i1][j1] != 0:
                return False
            i1 -= 1
            j1 -= 1

        i1 = i
        j1 = j
        while i1 < self.__size and j1 < self.__size:
            if self.__values[i1][j1] != 0:
                return False
            i1 += 1
            j1 += 1
        i1 = i
        j1 = j
        while i1 >= 0 and j1 < self.__size:
            if self.__values[i1][j1] != 0:
                return False
            i1 -= 1
            j1 += 1

        i1 = i
        j1 = j
        while i1 < self.__size and j1 >= 0:
            if self.__values[i1][j1] != 0:
                return False
            i1 += 1
            j1 -= 1

        return True

    def nextConfig(self, n):
        nextC = []

        for i in range(n):
            for j in range(n):
                if self.__values[i][j] == 0 and self.satisfyCond(i, j) == True:
                    aux = []
                    aux = [row[:] for row in self.__values]
                    aux[i][j] = 1
                    nextC.append(Configuration(aux))
        return nextC

    def __eq__(self, other):
        if not isinstance(other, Configuration):
            return False
        if self.__size != other.getSize():
            return False
        for i in range(self.__size):
            if self.__values[i] != other.getValues()[i]:
                return False
        return True

    def __str__(self):
        return str(self.__values)

    def checkFinal(self):
        #chceck if matrix satisfy all conditions for n-queens problem
        for i in range(self.__size):
            s = 0
            for j in range(self.__size):
                s += self.__values[i][j]
            if s != 1:
                return False
        for j in range(self.__size):
            s = 0
            for i in range(self.__size):
                s += self.__values[i][j]
            if s != 1:
                return False

        for i in range(self.__size):
            for j in range(self.__size):
                if self.__values[i][j] == 1:
                    i1 = i - 1
                    j1 = j - 1
                    while i1 >= 0 and j1 >= 0:
                        if self.__values[i1][j1] != 0:
                            return False
                        i1 -= 1
                        j1 -= 1

                    i1 = i + 1
                    j1 = j + 1
                    while i1 < self.__size and j1 < self.__size:
                        if self.__values[i1][j1] != 0:
                            return False
                        i1 += 1
                        j1 += 1
                    i1 = i - 1
                    j1 = j + 1
                    while i1 >= 0 and j1 < self.__size:
                        if self.__values[i1][j1] != 0:
                            return False
                        i1 -= 1
                        j1 += 1

                    i1 = i + 1
                    j1 = j - 1
                    while i1 < self.__size and j1 >= 0:
                        if self.__values[i1][j1] != 0:
                            return False
                        i1 += 1
                        j1 -= 1
        return True


class State:
    '''
    holds a PATH of configurations
    '''

    def __init__(self):
        self.__values = []

    def setValues(self, values):
        self.__values = values[:]

    def getValues(self):
        return self.__values[:]

    def __str__(self):
        s = ''
        for x in self.__values:
            s += str(x) + "\n"
        return s

    def __add__(self, something):
        aux = State()
        if isinstance(something, State):
            aux.setValues(self.__values + something.getValues())
        elif isinstance(something, Configuration):
            aux.setValues(self.__values + [something])
        else:
            aux.setValues(self.__values)
        return aux


class Problem:

    def __init__(self, initial):
        self.__initialConfig = initial
        # self.__finalConfig = final
        self.__initialState = State()
        self.__initialState.setValues([self.__initialConfig])
        self.__n = len(initial.getValues())

    def expand(self, currentState):
        myList = []
        currentConfig = currentState.getValues()[-1]
        for x in currentConfig.nextConfig(self.__n):
            myList.append(currentState + x)

        return myList

    def getRoot(self):
        return self.__initialState

    def heuristicsB(self, currentState):
        size = self.__n
        values = currentState.getValues()[-1].getValues()
        res = [[0 for x in range(size)] for y in range(size)]
        res[0][1] = 1
        if values == res and size % 2 == 0:
            return 1000
        res[0][1] = 0
        res[0][0] = 1
        if values == res and size % 2 == 1:
            return 1000

        suma = 0
        if size > 1:
            for i in range(size):
                for j in range(size):
                    suma += values[i][j]
            if suma >= 2:  # in order to have at least 2 elems;for 1 elems we use first 2 cases
                i = size - 1
                line = 0  # line and column where we found elem 1
                column = 0
                while i >= 0:
                    s = 0
                    for j in range(size):
                        s += values[i][j]
                        if values[i][j] == 1:
                            line = i
                            column = j
                    if s == 1:
                        if column > 1 and values[line - 1][column - 2] == 1:
                            return 1000
                        elif column <= 1 and size % 2 == column and values[line - 1][size - 1] == 1:
                            return 1000
                        else:
                            return -1000
                    i -= 1

        return -1000


class Controller:

    def __init__(self, problem):
        self.__problem = problem

    def DFS(self, root):
        if root.getValues()[-1].checkFinal() == True:
            return root  # currentState
        for r in self.__problem.expand(root):
            val = self.DFS(r)
            if val != False:
                return val
        return False


    def getBestChild(self, aux, node, visited):
        for x in self.__problem.expand(node):
            if x not in visited:
                aux.append(x)
        aux = [[x, self.__problem.heuristicsB(x)] for x in aux]
        aux.sort(key=lambda x: x[1], reverse=True)
        aux = [x[0] for x in aux]
        if len(aux) > 0:
            return [aux[0]]
        else:
            return []

    def Greedy(self, root):

        visited = []
        toVisit = [root]
        while len(toVisit) > 0:
            node = toVisit.pop(0)
            visited = visited + [node]
            if node.getValues()[-1].checkFinal() == True:
                return node
            aux = []

            aux1 = self.getBestChild(aux, node, visited)
            toVisit = aux1 + toVisit


class UI:

    def __init__(self):
        self.__iniC = Configuration([[0 for x in range(3)] for y in range(3)])
        self.__p = Problem(self.__iniC)
        self.__contr = Controller(self.__p)

    def printMainMenu(self):
        s = ''
        s += "0 - exit \n"
        s += "1 - read the number of lines and columns \n"
        s += "2 - find a path with DFS\n"
        s += "3 - find a path with Greedy\n"
        print(s)

    def readConfigSubMenu(self):
        n = 3
        try:
            print("Input the number (implicit n=3)")
            n = int(input("n = "))
        except:
            print("invalid number, the implicit value is still 3")
            n = 3
        self.__iniC = Configuration([[0 for x in range(n)] for y in range(n)])
        self.__p = Problem(self.__iniC)
        self.__contr = Controller(self.__p)

    def findPathDFS(self):
        startClock = time()
        r = self.__contr.DFS(self.__p.getRoot()).getValues()[-1].getValues()
        # print(r)

        if r != False:
            for i in r:
                print(i)
        else:
            print("THERE IS NO SOLUTION!")

        print('execution time = ', time() - startClock, " seconds")

    def findPathGreedy(self):
        startClock = time()
        r = self.__contr.Greedy(self.__p.getRoot()).getValues()[-1].getValues()
        if r != None:
            for i in r:
                print(i)
            # print("SOLUTION IS:",str(r))
        else:
            print("THERE IS NO SOLUTION!")
        print('execution time = ', time() - startClock, " seconds")

    def run(self):
        runM = True
        self.printMainMenu()
        while runM:
            try:
                command = int(input(">>"))
                if command == 0:
                    runM = False
                elif command == 1:
                    self.readConfigSubMenu()
                elif command == 2:
                    self.findPathDFS()
                elif command == 3:
                    self.findPathGreedy()
            except Exception:
                print("Invalid input")


def main():
    ui = UI()
    ui.run()


main()