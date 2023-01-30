#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        end = " "
        for idx, num in enumerate(row):
            if idx == len(row) - 1:
                end = ""
            print("{:d}".format(num), end=end)
        print("{}".format(""))
