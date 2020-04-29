from random import shuffle

class Repository:
    def __init__(self,file):
        self.l=[]
        self.train=[]
        self.test = []
        self.file=file
        self.readFile()

    def readFile(self):
        file = open(self.file, 'r')
        lines = file.readlines()
        for line in lines:
            self.l.append([line[0], int(line[2]), int(line[4]), int(line[6]), int(line[8])])
        shuffle(self.l)
        ind=int(0.9*len(self.l))
        self.train=self.l[:ind]
        self.test=self.l[ind:]
    def getTrain(self):
        return self.train
    def getTest(self):
        return self.test

