#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i_0 = 0
    i_1 = 0
    i_a = len(tuple_a) - 1
    i_b = len(tuple_b) - 1
    if (len(tuple_a) >= 2 and len(tuple_b) >= 2):
        i_0 = tuple_a[0] + tuple_b[0]
        i_1 = tuple_a[1] + tuple_b[1]
    elif (len(tuple_a) < 2 or len(tuple_b) < 2):
        i_0 = (0 if (i_a < 0) else tuple_a[0]) + (0 if i_b < 0 else tuple_b[0])
        i_1 = (0 if (i_a < 1) else tuple_a[1]) + (0 if i_b < 1 else tuple_b[1])
    return (i_0, i_1)
