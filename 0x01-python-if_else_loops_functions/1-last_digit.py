#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    store = number * -1
else:
    store = number
last_digit = store % 10
if number < 0:
    last_digit *= -1

if last_digit > 5:
    print(f"Last digit of {number:d} is {last_digit:d}"
          f" and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number:d} is {last_digit:d} and is 0")
else:
    print(f"Last digit of {number:d} is {last_digit:d}"
          f" and is less than 6 and not 0")
