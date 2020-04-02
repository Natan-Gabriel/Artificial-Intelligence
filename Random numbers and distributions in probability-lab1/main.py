import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.stats as stats
import random

def lcg(xn):
    (a, c, m) = (401, 101, 1024)  # (1103515245,12345,2**32)
    xn = (a * xn + c) % m
    return xn


def lcgList(n, x0, start, end):
    (a, c) = (401, 101)
    prs = [];
    xn = x0;
    for i in range(n):
        xn = (a * xn + c) % (end - start) + start;
        prs.append(xn);
    return prs;


def normalDistribution(arr):
    arr = np.array(arr)
    u = arr.mean()
    sig = arr.std()

    fd = []

    a = 0
    pi = math.pi
    for i in arr:
        a = ((i - u) ** 2) / (2 * (sig ** 2))
        e = math.exp(-a)
        fd.append((1 / (sig * math.sqrt(2 * pi))) * e)
    return fd


def logNormalDistribution(arr):
    arr = np.array(arr)
    u = arr.mean()
    sig = arr.std()

    fd = []

    a = 0
    pi = math.pi
    for i in arr:
        a = ((np.log(i) - u) ** 2) / (2 * (sig ** 2))
        e = math.exp(-a)
        fd.append((1 / (i * sig * math.sqrt(2 * pi))) * e)
    return fd


def exponentialDistribution(arr):
    arr = np.array(arr)
    u = 0.25

    fd = []

    a = 0
    for i in arr:
        a = u * i
        e = math.exp(-a)
        fd.append(u * e)
    return fd

def main(res):
    # print(a)
    while (1 == 1):
        print("1.Generate random number:")
        print("2.Normal Distribution generated by me:")
        print("3.Normal Distribution generated by computer:")
        print("4.Exponential Distribution generated by me:")
        print("5.Exponential Distribution generated by computer:")
        print("0.Break")
        a = input("a=")
        if (a == "1"):
            res = lcg(res)
            print(res)
        elif (a == "2"):
            start = input("First value of the interval=")
            end = input("Last value of the interval=")
            # arr = lcgList(5000,0,int(start),int(end))
            arr = lcgList(500, 0, int(start), int(end))
            arr.sort()
            y = normalDistribution(arr)
            plt.plot(arr, y)
            plt.show()
        elif (a == "3"):
            start = input("First value of the interval=")
            end = input("Last value of the interval=")
            x = np.linspace(int(start), int(end), 100)
            arr = np.array(x)
            u = arr.mean()
            sig = arr.std()
            plt.plot(x, stats.norm.pdf(x, u, sig))
            plt.show()
        elif (a == "4"):
            start = input("First value of the interval=")
            end = input("Last value of the interval=")
            arr = lcgList(500, 0, int(start), int(end))
            arr.sort()
            y = exponentialDistribution(arr)
            plt.plot(arr, y)
            plt.show()
        elif (a == "5"):
            start = input("First value of the interval=")
            end = input("Last value of the interval=")
            rv = stats.expon()
            distribution = np.linspace(int(start), int(end))
            plt.plot(distribution, rv.pdf(distribution))
            plt.show()
        elif (a == "0"):
            break
        else:
            return
main(0)