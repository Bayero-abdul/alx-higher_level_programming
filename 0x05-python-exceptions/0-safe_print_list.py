#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_elem = 0
    try:
        while num_elem < x:
            end = ""
            if num_elem == x - 1:
                end = '\n'

            print(my_list[num_elem], end=end)
            num_elem += 1
        return (num_elem)
    except IndexError:
        return (num_elem)
