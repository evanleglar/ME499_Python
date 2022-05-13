#!/bin/usr/env python3
import numpy as np
from random import random


def uniform_dist(n):  # average, standard dist, number of runs
    dist_sum = sum(np.random.uniform(0, 1, n))
    return dist_sum


print(uniform_dist(10))

