#!/usr/bin/python3
def uppercase(str):
    end = ""
    count = 1
    for char in str:
        if len(str) == count:
            end = '\n'

        if ord(char) >= 97 and ord(char) <= 122:
            print("{}".format(chr(ord(char) - 32)), end=end)
        else:
            print("{}".format(char), end=end)
        count += 1
