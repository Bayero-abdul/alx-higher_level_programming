#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_elem = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            num_elem += 1
        except IndexError:
            break

    print(my_list[i], end="")
    return (num_elem)
