#!/usr/bin/python3
def no_c(my_string):
    """removes all characters c and C from a string

        Arg:
            my_string: string to modify

        Return:
            returns a new string
    """
    letters = list(my_string)

    for i in range(len(letters)):
        if letters[i] == 'C' or letters[i] == 'c':
            letters[i] = ""

    return ("".join(letters))
