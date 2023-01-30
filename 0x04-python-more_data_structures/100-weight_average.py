#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return (0)

    score_weight = 0
    weight_sum = 0

    for t in my_list:
        score_weight += t[0] * t[1]
        weight_sum += t[1]

    return(score_weight/weight_sum)
