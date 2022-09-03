#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    argc = len(argv)
    if (argc == 1):
        print(f"0 arguments.")
    elif (argc == 2):
        print(f"1 argument:")
    else:
        print(f"{argc - 1} arguments:")

    for i in range(1, argc):
        print(f"{i}: {argv[i]}")
