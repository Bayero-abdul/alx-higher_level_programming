#!/usr/bin/python3
for num in range(97, 123):
    if chr(num) not in 'qe':
        print("{}".format(chr(num)), end="")
