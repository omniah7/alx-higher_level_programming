#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    argc = len(argv)
    print(f"{argc - 1} arguments", end='.\n' if argc == 1 else ':\n')

    for i in range(1, argc):
        print(f"{i}: {argv[i]}")
