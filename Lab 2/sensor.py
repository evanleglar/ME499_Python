#!/usr/bin/env python3


from math import sin
from random import gauss


def generate_sensor_data(n, sigma=0.01):
    """
    Generate data from a fake sensor.  These data are generated according to a sine function, with zero-mean
    Gaussian noise, with standard deviation sigma.
    """
    data = []
    for i in range(n):
        data.append(sin(i * 0.01) + gauss(0.0, sigma))
    return data


if __name__ == '__main__':
    # Print out a few of the numbers
    for d in generate_sensor_data(10):
        print(d)
