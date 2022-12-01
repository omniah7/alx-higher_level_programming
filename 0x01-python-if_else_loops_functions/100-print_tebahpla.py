#!/usr/bin/python3

for i, j in zip(range(122, 96, -2), range(121, 96, -2)):
    print(f"{chr(i).lower()}{chr(j).upper()}", end='')
