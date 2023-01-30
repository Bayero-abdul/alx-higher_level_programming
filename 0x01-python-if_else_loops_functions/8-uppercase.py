#!/usr/bin/python3
def uppercase(str):
    if str == "":
        print("")
    else:
        end = ""
        count = 1

        for char in str:
            if len(str) == count:
                end = '\n'

            print("{}".format(chr(ord(char) - 32) if ord(char) >= 97 and
                  ord(char) <= 122 else char), end=end)
            count += 1
