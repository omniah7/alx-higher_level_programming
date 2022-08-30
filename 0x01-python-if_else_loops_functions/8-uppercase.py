#!/usr/bin/python3
def uppercase(str):
    tmp = list(str)
    i = 0
    for c in tmp:
        if (ord(c) >= ord('a')) and (ord(c) <= ord('z')):
            tmp[i] = chr(ord(c) - ord('a') + ord('A'))
        i += 1
    print(f"{''.join(tmp)}")
