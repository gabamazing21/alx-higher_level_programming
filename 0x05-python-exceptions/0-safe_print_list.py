def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        elem_count = 0
        for i in my_list:
            count += 1
        for i, j in enumerate(my_list):
            if ((i + 1) <= x):
                print(j, end='')
                elem_count += 1
        print()
    except Exception:
        print("we have an error")
    return elem_count
