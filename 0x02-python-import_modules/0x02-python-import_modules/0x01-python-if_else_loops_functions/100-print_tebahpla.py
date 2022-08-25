#!/usr/bin/python3
count = 1
for num in range(122, 96, -1):
    if count % 2 == 0:
        num = num - 32

    print("{}".format(chr(num)), end="")
    count += 1
