#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list

        Arg:
            my_list: list of integers

        Returns:
            Return a new list with True or False,
            depending on whether the integer at the
            same position in the original list is a multiple of 2
    """

    new_list = [num % 2 == 0 for num in my_list]
    return new_list
