#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_num = 0
    for i in set(my_list):
        sum_num += i
    return sum_num
