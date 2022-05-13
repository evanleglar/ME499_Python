#!/bin/usr/env/python3
import subprocess
import random
import numpy as np
from scipy import optimize
from matplotlib import pyplot as plt


class Simulator:

    def __init__(self, input):
        self.input = input

    def evaluate(self, points, file_name='waypoints.txt'):
        if points[0] != (-10, -10) or points[-1] != (10, 10):
            raise ValueError("Invalid list of starting and end points")
        else:
            points_list = []

            for i in points:
                points_list.append(str(i[0]) + ' ' + str(i[1]) + '\n')

            with open(file_name, 'w+') as f:
                f.writelines(points_list)

            output = subprocess.check_output(['./simulator-mac', file_name, str(self.input)])
            decoded_output = output.decode("utf-8")
            path_cost = decoded_output.split('is')[1].split('.\\')[0].strip('.\n')

            return float(path_cost)

    def search_random(self, n):
        rand_points = []

        for i in range(n):
            rand_points.append([random.uniform(-10, 10), random.uniform(-10, 10)])

        coord_test = []
        for j in rand_points:
            new_coords = [(-10, -10), j, (10, 10)]
            coord_test.append(self.evaluate(new_coords, "waypoints.txt"))

        return min(coord_test), rand_points[coord_test.index(min(coord_test))]

    def search_grid(self, n):
        if n < 2:
            raise ValueError('n must be >= 2')
        else:
            linear_pts = []
            k = np.linspace(-10, 10, n+1)
            for i in k:
                for j in k:
                    pt = i, j
                    linear_pts.append(pt)

            coord_test = []
            for j in linear_pts:
                new_coords = [(-10, -10), j, (10, 10)]
                coord_test.append(self.evaluate(new_coords, "waypoints.txt"))

        return min(coord_test), linear_pts[coord_test.index(min(coord_test))]

    def search_fmin(self):
        func = lambda x: self.evaluate([(-10, -10)] + [x] + [(10, 10)])
        f_optim = optimize.fmin(func=func, x0=(0, 0), maxiter=200, maxfun=200, full_output=True)
        return f_optim[1], tuple(f_optim[0]), f_optim[3]
#     returns cost, optimized point, # of function evaluations

    def compare_fmin_versus_random(self, n):
        rand_values = []
        fmin_values = []
        num_fmin_evals = 0

        for i in range(n):
            fmin = self.search_fmin()
            fmin_values.append(fmin[0])
            num_fmin_evals = fmin[2]
            rand_values.append(s.search_random(num_fmin_evals)[0])

        return fmin_values, rand_values, num_fmin_evals

    def search_fmin_multi(self, n, max_iter=500):
        linear_pts = [(-10, -10)]
        k = np.linspace(-10, 10, n + 1)
        for i in k:
            for j in k:
                pt = i, j
                linear_pts.append(pt)
        linear_pts.append((10, 10))

        print(linear_pts)

if __name__ == '__main__':
    w = [(-10, -10), (0, 2), (10, 10)]
    instance = 24
    s = Simulator(instance)
    # print(s.evaluate(w))
    # print(s.search_random(100))
    # print(s.search_grid(10))
    # print(s.search_fmin())

    # problem #3
    # n = 50
    # fmin_values, rand_values, num_evals = s.compare_fmin_versus_random(n)
    # n_list = list(range(1, n+1))
    # plt.plot(n_list, fmin_values, label='Fmin Search')
    # plt.plot(n_list, rand_values, label='Random Search')
    # plt.xlabel('Number of Evaluations')
    # plt.ylabel('Cost of Path')
    # plt.legend()
    # plt.title(f'Comparing Fmin vs. Random Searching of Radiation Environment \n '
    #           f'Problem Instance {instance} with {n} Evaluations')
    # plt.savefig(f'comparison_problem_{instance}_n_{n}.png', bbox_inches='tight')

    s.search_fmin_multi(3)