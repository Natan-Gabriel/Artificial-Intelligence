from Controller import Controller
from FuzzyVariable import FuzzyVariable
from Repo import Repo


def trapezoid(a, b, c, d):
    return lambda x: max(0, min((x - a) / (b - a), 1, (d - x) / (d - c)))


def triangle(a, b, c):
    return trapezoid(a, b, b, c)


def inverseLine(a, b):
    return lambda val: val * (b - a) + a


def inverseTriangle(a, b, c):
    return lambda val: (inverseLine(a, b)(val) + inverseLine(c, b)(val)) / 2




def main():
    temperature = FuzzyVariable()
    humidity = FuzzyVariable()
    time = FuzzyVariable()

    temperature.addMembershipFunction('very cold', trapezoid(-1000, -30, -20, 5))
    temperature.addMembershipFunction('cold', triangle(-5, 0, 10))
    temperature.addMembershipFunction('normal', trapezoid(5, 10, 15, 20))
    temperature.addMembershipFunction('warm', triangle(15, 20, 25))
    temperature.addMembershipFunction('hot', trapezoid(25, 30, 35, 1000))

    humidity.addMembershipFunction('dry', triangle(-1000, 0, 50))
    humidity.addMembershipFunction('normal', triangle(0, 50, 100))
    humidity.addMembershipFunction('wet', triangle(50, 100, 1000))

    time.addMembershipFunction('short', triangle(-1000, 0, 50), inverseLine(50, 0))
    time.addMembershipFunction('medium', triangle(0, 50, 100), inverseTriangle(0, 50, 100))
    time.addMembershipFunction('long', triangle(50, 100, 1000), inverseLine(50, 100))

    repo=Repo()
    ctrl = Controller(temperature, humidity, time, repo.getData())


    a=ctrl.compute({'humidity': 65, 'temperature': 17})
    b=ctrl.compute({'humidity': 50, 'temperature': 5})
    c=ctrl.compute({'humidity': 0, 'temperature': 20})
    d=ctrl.compute({'humidity': 75, 'temperature': 20})
    repo.writeToFile([a,b,c,d])

    print(a)
    print(b)
    print(c)
    print(d)

main()
