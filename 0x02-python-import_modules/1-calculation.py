#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    plus = a + b
    minus = a - b
    mult = a * b
    div = int(a / b)
    print("{} + {} = {}".format(a, b, plus))
    print("{} - {} = {}".format(a, b, minus))
    print("{} * {} = {}".format(a, b, mult))
    print("{} / {} = {}".format(a, b, div))
