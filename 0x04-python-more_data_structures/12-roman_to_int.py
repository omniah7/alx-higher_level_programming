#!/usr/bin/python3
def roman_to_int(roman):
    if roman is None:
        return 0
    nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    sum = 0
    for i in range(len(roman)):
        if roman[i] is 'I' and roman[i+1] in "VX":
                i = i + 1
                sum += nums[roman[i]] - 1
                continue
        sum += nums[roman[i]]
    return sum
