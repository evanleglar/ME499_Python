#!/usr/bin/env python3

f = lambda x: len(x)

lst = [[0],[2,4,5],[3,4]]

print(max(lst, key=f))