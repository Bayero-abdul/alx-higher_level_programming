#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element from a list

        Args:
            mylist: list of integers
            idx: index

        Returns:
            returns None if idx < 0 or idx > number of elements
            in my_list.
            else returns element at index idx
    """

    if idx < 0:
        return (None)
    if idx > len(my_list):
        return (None)

    return (my_list[idx])
