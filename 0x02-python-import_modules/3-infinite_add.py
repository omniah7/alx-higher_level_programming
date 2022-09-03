#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    intlist = [int(argv[i]) for i in range(1, len(argv))]
    print(sum(intlist))
