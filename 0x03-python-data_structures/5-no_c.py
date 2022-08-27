#!/usr/bin/python3
def no_c(my_string):
    for char in my_string:
        if char in 'Cc':
            idx = list(my_string).index(char)
            if idx == len(my_string) - 1:
                new_string = my_string[:idx]
            else:
                my_string = my_string[:idx] + my_string[idx + 1:]

    return (my_string)
