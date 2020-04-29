from collections import Counter
from math import log

from Node import Node


class Controller:
    def __init__(self,repo):
        self.repo=repo

    def most_frequent(self,l):
        return max(set(l), key=l.count)

    def generate(self,d, attr):  # //D – a partitioning of training data, A – list of attributes(POSITIONS OF)
        node = Node()
        cls = d[0][0]
        for i in d:
            if i[0] != cls:
                cls = -1
        if cls != -1:
            node.label = cls
            # print(node.label)
            node.leaf = 1
            return node
        else:
            if not attr:
                node.label = self.most_frequent([n[0] for n in d])
                # print(node.label)
                node.leaf = 1
                return node
            else:
                separation_attribute = self.getBestAtr(d, attr)  # choice(attr)
                node.label = separation_attribute
                for i in range(1, 6):
                    dj = [x for x in d if x[separation_attribute] == i]
                    node.attribute = separation_attribute
                    node.value = i
                    if not dj:
                        n = Node()
                        n.label = self.most_frequent([n[0] for n in d])
                        n.leaf = 1
                        n.value = i
                        node.children.append(n)
                    else:
                        n = self.generate(dj, [x for x in attr if x != separation_attribute])
                        n.value = i
                        node.children.append(n)
                return node


    def getBestAtr(self,d, attr):
        max = attr[0]
        for i in attr:
            if (self.gain(d, i) < self.gain(d, max)):
                max = i
        return max
    def gain(self,s, a):
        '''
        return the information gain:
        gain(s, a) = entropy(s)− SUM ( |Sv| / |S| * entropy(Sv) )
        '''
        # sv = [x for x in s if x[a] == v]
        ValuesA = [x[a] for x in s]
        ValuesA = list(set(ValuesA))
        total = 0
        for v in ValuesA:
            sv = [x for x in s if x[a] == v]
            total += len(sv) / len(s) * self.entropy(sv)

        gain = self.entropy(s) - total
        return gain
    def entropy(self,pi):
        total = 0
        pi2=[x[0] for x in pi]
        chi=list(Counter(pi2).values())
        for p in chi:
            p = p / sum(chi)
            if p != 0:
                total += p * log(p, 2)
            else:
                total += 0
        total *= -1
        return total

    def test(self,elem,root):
        r=root
        while True:
            for child in r.children:
                attr = r.label
                if child.leaf==-1 and elem[attr]==child.value:#root.label:
                    r=child
                elif child.leaf!=-1:#elem[attr-1]==child.value:
                    return child.label#leaf
