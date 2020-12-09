from FuzzyRule import FuzzyRule


class Repo:
    def __init__(self):
        self.fileName = 'input.in'
        self.data = []
        self.readFile()

    def readFile(self):
        file = open(self.fileName, 'r')
        lines = file.readlines()
        index = 0
        for line in lines:

            f_list = [i for i in line.split(",")]
            self.data.append(FuzzyRule(
                {f_list[0] : f_list[1], f_list[2]: f_list[3]}, {f_list[4] : f_list[5]}))
            #self.output.append([float(f_list[5])])
            #print(self.data)
            index += 1
    def getData(self):
        return self.data

    def writeToFile(self,l):
        open('file.txt', 'w').close()
        with open('output.out', 'w') as f:
            for item in l:
                f.write("%s\n" % item)