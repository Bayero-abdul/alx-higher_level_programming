#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order

        Arg:
            my_list: list of integers

        Returns: void
    """
    if my_list != []:
        for i in reversed(my_list):
            print("{}".format(i))
