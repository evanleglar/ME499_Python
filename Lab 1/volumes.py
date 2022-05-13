#!/usr/bin/env python
from math import pi


def cylinder_volume(radius, height):
    if radius <= 0:
        raise ValueError
    if height <= 0:
        raise ValueError
    else:
        return pi * radius**2 * height


def torus_volume(r_inner, r_outer):

    r_maj = (r_outer + r_inner) / 2
    r_min = (r_outer - r_inner) / 2

    if r_outer < 0:
        raise ValueError
    if r_inner < 0:
        raise ValueError
    if r_maj < 0:
        raise ValueError
    if r_min < 0:
        raise ValueError
    else:
        return 2 * (pi ** 2) * r_maj * (r_min ** 2)


if __name__ == '__main__':
    print(cylinder_volume(4, 2))
    print(pi * 4**2 * 2)
    print(torus_volume(3, 4))
    print(17.27)  # volume of torus from torus.py tested values of r_minor = 3, r_major = 4
