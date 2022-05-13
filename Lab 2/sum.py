#!/usr/bin/env python


def sum_i(l):

    total1 = 0

    for i in range(0, len(l)):
        total1 += l[i]
    return total1


def sum_r(l):

    if len(l) == 1:
        return l[0]
    else:
        return l[0] + sum_r(l[1:])


if __name__ == '__main__':
    l = [1, 2, 3, 4]
    print("iterative sum of all the elements in the list is ", sum_i(l))
    print("recursive sum of all the elements in the list is ", sum_r(l))
    print("using built-in sum of all the elements in the list is ", sum(l))
