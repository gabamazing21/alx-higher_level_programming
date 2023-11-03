#!/usr/bin/python3
from sys import argv
if (__name__ == '__main__'):
    arg_num = len(argv) - 1
    if (arg_num < 1):
        print(f"{arg_num} arguments.")
    elif (arg_num == 1):
        print(f"{arg_num} argument:")
        print(f"{arg_num}: {argv[arg_num]}")
    elif (arg_num > 1):
        for i in range(1, len(argv)):
            print(f"{arg_num} arguments:")
            print(f"{i}: {argv[i]}")
