#!/usr/bin/env python
from math import gcd as old_gcd
from random import randint


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == '__main__':

    counter = 0  # how many successful trials of new gcd function

    for i in range(0, 1001):
        a, b = randint(1, 1 * 10 ** 6), randint(1, 1 * 10 ** 6)

        if gcd(a, b) != old_gcd(a, b):
            print('Function Failed')
            counter = counter - 1
            raise ValueError

        else:
            counter = counter + 1
    print(str(counter) + str(' successful gcd computations'))




