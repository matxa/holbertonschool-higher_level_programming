#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    operators = ['+', '-', '*', '/']
    func = None
    if len(argv) - 1 == 3:
        a = int(argv[1])
        op = argv[2]
        b = int(argv[3])
        if op == operators[0]:
            func = add(a, b)
        elif op == operators[1]:
            func = sub(a, b)
        elif op == operators[2]:
            func = mul(a, b)
        elif op == operators[3]:
            func = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator>")
        exit(1)
    print("{:d} {} {:d} = {:d}".format(a, op, b, func))
