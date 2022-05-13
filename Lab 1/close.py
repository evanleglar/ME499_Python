#!/usr/bin/env python


def close(num_1, num_2, diff):
    if abs(num_1 - num_2) <= diff:
        return True
    else:
        return False


if __name__ == '__main__':
    print(close(1, 2, 0.5))
    print(close(1, 2, 3))
