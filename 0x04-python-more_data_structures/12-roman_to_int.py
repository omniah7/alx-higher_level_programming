#!/usr/bin/python3
def roman_to_int(roman):
    if roman is None or not isinstance(roman, str):
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
    sum = nums[roman[0]]
    for i in range(1, len(roman)):

        if roman[i] in "VX" and roman[i-1] == 'I':
            sum += nums[roman[i]] - 2 * nums['I']
            continue
        if roman[i] in "CL" and roman[i-1] == 'X':
            sum += nums[roman[i]] - 2 * nums['X']
            continue
        if roman[i] in "DM" and roman[i-1] == 'C':
            sum += nums[roman[i]] - 2 * nums['C']
            continue
        sum += nums[roman[i]]
    return sum
