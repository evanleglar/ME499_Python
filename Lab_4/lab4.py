#!/usr/bin/env python3

from math import pi as pi
import numpy as np
import matplotlib.pyplot as plt
from problem2 import uniform_dist
from timeit import default_timer as timer
import random as random

from msd import MassSpringDamper

"""Problem 1: Sine wave plot"""
x = np.linspace(0, 4*pi, 50)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel("Pi Time")
plt.ylabel("Amplitude")
plt.title("Lab 4, Problem 1, Plot a Sine Wave")
plt.axis([0, 4*pi, -1.2, 1.2])
plt.show()

"""Problem 2: Histogram of Uniform Distribution Samples"""
dist_list = []

for i in range(10000):
    dist_list.append(uniform_dist(10))
plt.hist(dist_list, 100, density=1, facecolor='g', alpha=0.75)
plt.xlabel("Sum of 10 Random Samples Between 0 and 1")
plt.ylabel("Probability Density")
plt.title("Lab 4, Problem 2, Plot a Histogram")
plt.axis([0, 10, 0, 0.6])
plt.show()

"""Problem 3: Plotting Mass Spring Damper System"""
smd = MassSpringDamper(m=10, k=10, c=1)
state, t = smd.simulate(0.0, 1.0)
pos = [line[0] for line in state]
plt.plot(t, pos, label='Position')
plt.xlabel("Time")
plt.ylabel("State (position/velocity)")
plt.title("Lab 4, Problem 3, Plot Mass Spring Damper")
plt.axis([0, 4*pi, -1.2, 1.2])
plt.show()

"""Problem 4: Sorting Times"""
sortlength = [10**x for x in range(7)]
timelist_sort = []
timelist_sum = []

for i in sortlength:
    randomlist1 = random.sample(range(0, i*2), i)
    start = timer()
    sorted(randomlist1)
    end = timer()
    time2exec = end-start
    timelist_sort.append(time2exec)

for i in sortlength:
    randomlist2 = random.sample(range(0, i * 2), i)
    start = timer()
    sortedlist = sum(randomlist2)
    end = timer()
    time2exec = end - start
    timelist_sum.append(time2exec)

plt.plot(sortlength, timelist_sort, label="Sort Time")
plt.plot(sortlength, timelist_sum, label="Sum time")
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

plt.xlabel("Length of Sorted List (n)")
plt.ylabel("Time to Execute Sort Function (Seconds)")
plt.title("Lab 4, Problem 4, Execution Speed of Sort Function vs. Size")
plt.xscale("log")
plt.legend()
plt.show()

