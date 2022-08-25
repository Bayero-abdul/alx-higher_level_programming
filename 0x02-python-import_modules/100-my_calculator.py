#!/usr/bin/python3
def main():
    from sys import exit, argv
    from calculator_1 import add, mul, sub, div

    if len(argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    sign = argv[2]

    if sign not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if sign == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif sign == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif sign == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))

    exit(0)


if __name__ == "__main__":
    main()
