#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    if len(argv) == 4:
        list = []
        for i in argv[1:]:
            list.append(i)
        op = argv[2]
        a = int(list[0])
        b = int(list[2])
        if op in operators:
            if op == '+':
                print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
            elif op == '-':
                print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
            elif op == '*':
                print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
            elif op == '/':
                print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        exit(0)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
