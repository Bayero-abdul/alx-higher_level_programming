#!/usr/bin/python3
zero = 0
for num in range(100):
    if num > 9:
        zero = ''

    if num == 99:
        print("{0}{1:d}".format(zero, num))
    else:
        print("{0}{1:d}, ".format(zero, num), end="")
