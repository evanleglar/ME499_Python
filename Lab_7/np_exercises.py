#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt


def numpy_close(a, b, tol=1e-8):

    if a.shape == b.shape and np.allclose(a, b, atol=tol):
        return True
    else:
        return False


def minimize_pow(n):
    x = np.linspace(0, 1, n)
    f = x ** x
    ind = np.argmin(f)
    x = x[ind]
    y = f[ind]
    return x, y


def simulate_dice_rolls(num_rolls, iterations):
    k = np.random.randint(1, 7, size=(num_rolls, iterations)).sum(axis=0)
    plt.hist(k)
    plt.savefig(f'dice_{num_rolls}_rolls_{iterations}.png', bbox_inches='tight')


def nearest_neighbors(array, point, dist):
    dist_arry = np.linalg.norm(abs(array - point), axis=1) <= dist
    true_nums = array[dist_arry]
    sorted_dist = np.argsort(np.linalg.norm(abs(true_nums - point), axis=1))
    true_nums = true_nums[sorted_dist]

    return true_nums


if __name__ == '__main__':
    u = np.array([[1, 2], [2, 4, np.NaN]])
    v = np.array([[1, 2], [2, 4, np.NaN]])
    print(numpy_close(u, v))
    print(minimize_pow(100))
    print(simulate_dice_rolls(1, 100))
    test_points = np.array([[1, 1, 1], [2, 3, 5], [0, 1, 1], [1.5, 1, 1], [10, 9, 9]])
    target_pt = np.array([0, 1, 1])
    p4 = nearest_neighbors(test_points, target_pt, 3.0)
    print(p4)
