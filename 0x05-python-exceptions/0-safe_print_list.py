#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num_elem = 0
        for i in range(x):
            if type(my_list[i]) is int:
                end = ""
                if i == x - 1:
                    end = '\n'
            
                print(my_list[i], end=end)
                num_elem += 1
        return (num_elem)
    except IndexError:
        return (num_elem)
