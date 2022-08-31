#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    max_num = 0
    for key in a_dictionary:
        if a_dictionary[key] >= max_num:
            max_num = a_dictionary[key]
            best_student = key
    return (best_student)
