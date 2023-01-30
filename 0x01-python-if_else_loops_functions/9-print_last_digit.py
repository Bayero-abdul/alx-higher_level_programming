#!/usr/bin/python3
def print_last_digit(number):
    """Prints and returns the value of the last digit"""
    if number < 0:
        number *= -1
    print("{0:d}".format(number % 10), end="")
    return (number % 10)
