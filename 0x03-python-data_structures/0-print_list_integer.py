#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Prints all integers of a list

        Arg:
            my_list: list of integers

        Returns: void
    """

    for i in my_list:
        print("{:d}".format(i))
