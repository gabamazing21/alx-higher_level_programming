#!/usr/bin/python3
def custom_zip_longest(iter1, iter2, fillValue=None):
    iter1_exhausted = object()
    iter2_exhausted = object()
    for i in range(max(len(iter1), len(iter2))):
        val1 = iter1[i] if i < len(iter1) else iter1_exhausted
        val2 = iter2[i] if i < len(iter2) else iter2_exhausted
        if val1 is iter1_exhausted:
            yield (fillValue, val2)
        elif val2 is iter2_exhausted:
            yield (val1, fillValue)
        else:
            yield (val1, val2)


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    div, count = 0, 0
    wrong_type = False
    try:
        for item1, item2 in (custom_zip_longest
                             (my_list_1, my_list_2, fillValue=0.0)):
            if (count > list_length):
                break
            if (type(item1) is not int) or (type(item2) is not int):
                div = 0
                wrong_type = True
            elif (item2 == 0):
                div = 0
                print("division by 0")
            elif (item1 % item2 != 0):
                div = 0
                print("not divible")
            else:
                div = item1 / item2
            count += 1
            new_list.append(div)
        if (len(my_list_1) != len(my_list_2)):
            print("out of range")
        if (wrong_type):
            print("wrong type")
        return new_list
    except Exception:
        print("we have an error")
    finally:
        return new_list
