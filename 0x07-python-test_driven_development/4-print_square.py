#!/usr/bin/python3
def print_square(size):
    """prints square."""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        end = ""
        for j in range(size):
            if j == size - 1:
                end = '\n'
            print("#", end=end)
