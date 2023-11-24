#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None
    except Exception:
        return None
    finally:
        if(a/b):
            print("Inside result: {}".format(a/b))
            return a/b
        else:
            print("Inside result: None")
            return None
