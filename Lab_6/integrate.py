#!/usr/bin/env python3
from numpy import linspace, sqrt, pi
import random
import matplotlib.pyplot as plt


def integrate(f, a, b, n=100):
    a = float(a)
    b = float(b)
    x = linspace(min(a, b), max(a, b), n)
    integral = 0

    for i in range(1, n-1):
        integral += f(x[i])*((b-a)/n)

    return integral


def integrate_mc(f, a, b, bound_lower, bound_upper, n=100):
    a = float(a)
    b = float(b)

    point_cntr = 0

    monte_area = abs(a - b) * abs(bound_upper - bound_lower)

    for j in range(1, n):
        x = min(a, b) + abs(b - a) * random.random()
        y = bound_lower + ((bound_upper - bound_lower) * random.random())

        if f(x) > 0 and 0 < y <= f(x):
            point_cntr += 1
        if f(x) < 0 and 0 > y >= f(x):
            point_cntr -= 1

    integral_mc = monte_area * float(point_cntr) / n

    return integral_mc


def estimate_pi(n):
    counter = 0

    x = linspace(-1, 1, n)
    y = linspace(-1, 1, n)

    for i in x:
        for j in y:
            if sqrt((i*i + j*j)) < 1:
                counter += 1
            else:
                counter += 0

    pi_estimate = 4 * counter / (n*n)
    square_normalized = (4 / pi) * pi_estimate
    return pi_estimate, square_normalized


if __name__ == '__main__':
    f = lambda x: 2 * x * x  # test with 2x2
    a = 0
    b = 1
    n = 100
    x = linspace(a, b, n)
    bound_upper_1 = max(f(x))
    bound_lower_1 = min(f(x))

    print(integrate(f, a, b, n))
    print(integrate_mc(f, a, b, bound_lower_1, bound_upper_1, n))
    print(estimate_pi(1000))

# """ problem 4"""
    h_func = lambda x: x ** 3 + 2 * x - 1
    inc = [x for x in range(1, 1001) if x % 10 == 0]

    reimann_vals = []
    monte_vals = []

    for i in inc:
        c = linspace(a, b, i)
        bound_lower_2 = max(h_func(c))
        bound_upper_2 = min(h_func(c))
        monte_vals.append(integrate_mc(h_func, a, b, bound_lower_2, bound_upper_2, i))
        reimann_vals.append(integrate(h_func, a, b, i))

    print(monte_vals)

    plt.plot(inc, reimann_vals, label="ReimannSumValue")
    plt.plot(inc, monte_vals, label="MonteCarloValue")

    plt.xlabel("# of Evaluations")
    # plt.axis([0, 1000, 0, 0.6])
    plt.ylabel("Calculated Integral")
    plt.title("Problem 4: Plotting Integral Method Convergence")
    plt.hlines(0.25, 0, 1050, colors='k', linestyles='dotted', label='Definite Integral = 0.25')
    plt.legend()

    plt.show()
