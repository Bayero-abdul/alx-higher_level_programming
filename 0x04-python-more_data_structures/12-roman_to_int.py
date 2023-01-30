#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)

    rom_to_int = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
    sum_num = 0
    first_num = rom_to_int[roman_string[0]]
    cluster_sum = first_num
    prev_num = first_num
    counter = 0

    for i in range(1, len(roman_string)):
        curr_num = rom_to_int[roman_string[i]]
        if curr_num <= prev_num:
            cluster_sum += curr_num
        else:
            cluster_sum = abs(cluster_sum - curr_num)

        prev_num = curr_num

        if i + 1 < len(roman_string):
            next_num = rom_to_int[roman_string[i + 1]]
            if (counter == 1 or counter == 2 or counter == 3 and curr_num != next_num) or (first_num == curr_num and counter == 0):
                counter = 0
                sum_num += cluster_sum
                print(f"cluster_sum: {cluster_sum}")
                cluster_sum = 0
            else:
                counter = counter + 1

    sum_num += cluster_sum
    print(f"cluster_sum: {cluster_sum}")
    return (sum_num)
