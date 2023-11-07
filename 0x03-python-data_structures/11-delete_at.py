#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    i = len(my_list) - 1
    if (idx > i or i < 0):
        return (my_list)
    else:
        for index, j in enumerate(my_list):
            if (index == idx):
                del my_list[index]
                return my_list
