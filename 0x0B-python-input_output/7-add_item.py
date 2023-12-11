#!/usr/bin/python3
""" This module provide fuction to perfor commandline json manipulation"""
import sys
import json
import os


def main(*argc, **argv):
    """This function takes input from commandline to a json file"""
    save_to_json_file = (__import__('5-save_to_json_file').
                         save_to_json_file)
    load_from_json_file = (__import__('6-load_from_json_file').
                           load_from_json_file)
    argv = sys.argv[1:]
    file_name = "add_item.json"
    current_path = os.getcwd()
    if (os.path.exists(f"{current_path}/{file_name}")):
        argv = argv + load_from_json_file(file_name)
        save_to_json_file(argv, file_name)
    else:
        save_to_json_file(argv, file_name)


if __name__ == "__main__":
    main()
