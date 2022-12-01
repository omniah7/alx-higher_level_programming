#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv
    
    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    opr = argv[2]
    if opr not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a, b = int(argv[1]), int(argv[3])
    ops = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div,
    }

    print(f"{a} {opr} {b} = {ops[opr](a, b)}")



