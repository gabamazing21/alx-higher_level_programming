#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_tuple_a = 0
    sum_tuple_b = 0
    if (len(tuple_a) == 0):
        sum_tuple_a = 0
    elif (len(tuple_a) < 2):
        sum_tuple_a = tuple_a[0] + 0
    else:
        for index, i in enumerate(tuple_a):
            if (index >= 2):
                break
            sum_tuple_a += i

    if (len(tuple_b) == 0):
        sum_tuple_b = 0
    elif (len(tuple_b) < 2):
        sum_tuple_b = tuple_b[0] + 0
    else:
        for index, i in enumerate(tuple_b):
            if (index >= 2):
                break
            sum_tuple_b += i
    return (sum_tuple_a, sum_tuple_b)
