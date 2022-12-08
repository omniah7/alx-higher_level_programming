#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    x = [my_list[x][0] for x in range(len(my_list))]
    y = [my_list[y][1] for y in range(len(my_list))]
    return sum(list(map(lambda x, y: x*y, x, y)))/sum(y)
