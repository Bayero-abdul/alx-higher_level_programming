#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """replaces an element of a list at a specific position

        Args:
            mylist: list of integers
            idx: index
            element: new element

        Returns:
            returns original list if idx < 0 or idx > number of elements
            in my_list,
            else returns modified list
    """

    if idx < 0:
        return (my_list)
    if idx > len(my_list):
        return (my_list)

    my_list[idx] = element
    return (my_list)
