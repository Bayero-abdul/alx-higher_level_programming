#!/usr/bin/python3
def max_integer(my_list=[]):
    """finds the biggest integer of a list

        Arg:
            my_list: list of integers

        Returns:
            the biggest integer of a list
    """

    if list == []:
        return None

    max = 0
    for num in my_list:
        if num > max:
            max = num

    return max
