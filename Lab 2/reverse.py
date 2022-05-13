#!/usr/bin/env python


def reverse_i(l):
    if range(len(l)) == 0:
        return 0
    else:
        for i in l[:: -1]:
            if i == 0:
                return l[0]
            else:
                print(i)


def reverse_r(l):

    if not l:
        return []
    else:
        return [l[-1]] + reverse_r(l[:-1])


if __name__ == '__main__':
    # l = [1, 2, 3, 4]
    l = "hello"

    print(reverse_i(l))
    print(reverse_r(l))
