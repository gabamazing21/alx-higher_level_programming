#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        inner_count = 0
        for i in my_list:
            count += 1
        if (x > count):
            raise IndexError
        for i, j in enumerate(my_list):
            if ((i + 1) <= x):
                if type(j) is not int:
                    continue
                else:
                    print("{:d}".format(j), end='')
                    inner_count += 1
        print()
        return inner_count
    except (IndexError):
        print("list index out of range")
