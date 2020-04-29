from collections import Counter
from copy import deepcopy
from itertools import count
from math import log
from random import choice, randint, shuffle

from Controller import Controller
from Repository import Repository

class UI:
    def loop(self):
        self.repo = Repository('balance-scale.data')
        self.ctrl = Controller(self.repo)
        root = self.ctrl.generate(self.repo.getTrain(), [1, 2, 3, 4])
        total=0
        sum=0
        for i in self.repo.getTest():
            if(self.ctrl.test(i,root)==i[0]):
                sum+=1
            total+=1
        return sum/total


    def run(self):
        best=0
        ind=0
        iter=0
        while iter<30000:
            ind = self.loop()
            if ind > best:
                best=ind
                if best>0.5:
                    print(best)
            iter+=1
        print("Best accuracy",best)


ui=UI()
ui.run()


