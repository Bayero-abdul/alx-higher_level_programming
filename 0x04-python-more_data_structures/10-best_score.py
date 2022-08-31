#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    else:
        sorted_dict = sorted(a_dictionary.items(), key=lambda k: k[1])
        best_student = sorted_dict[0][1]

        return (best_student)
