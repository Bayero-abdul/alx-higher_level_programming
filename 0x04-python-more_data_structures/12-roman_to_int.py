#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not(isinstance(roman_string, str))) or roman_string is None:
        return (0)

    rom_to_int = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
    sum_num = rom_to_int[roman_string[0]]
    prev_num = sum_num

    for i in range(1, len(roman_string)):
        curr_num = rom_to_int[roman_string[i]]
        if curr_num <= prev_num:
            sum_num += curr_num
        else:
            sum_num = abs(sum_num - curr_num)
        prev_num = curr_num

    return (sum_num)
