#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers

        Arg:
            matrix: list of list of integers

        Returns: void
    """
    if matrix == [[]]:
        print()
    else:
        for row in matrix:
            for i, elem in enumerate(row):
                if i == 2:
                    print("{:d}".format(elem))
                else:
                    print("{:d}".format(elem), end=" ")
