#!/usr/bin/python3
def print_square(size):
    """prints square."""
    if type(size) != int:
        raise TypeError("size must be integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    
    if size == 0:
        print("")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
                if i != size - 1:
                    print('\n')
