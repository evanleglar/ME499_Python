#!/usr/bin/env python3

import sys

program = sys.argv[0]
rest = sys.argv[1:]

print(program)
print(rest)

# number = int(sys.argv[1])
# for i in range(number):
#     print(i)


vehicle = {}

vehicle["car"] = 2
vehicle["truck"] = 5
vehicle["bike"] = 1

print(vehicle["car"])

for i in vehicle:
    # print(i)
    print(vehicle[i]) #  how to get
