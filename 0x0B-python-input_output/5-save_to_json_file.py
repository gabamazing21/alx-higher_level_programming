#!/usr/bin/python3
"""
this module
write object to
text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - write to textfile in json
    parameter:
    my_obj - object to write (string)
    filename - name of text file (string)
    """
    with open(filename, 'w', encoding="UTF-*") as f:
        f.write(json.dumps(my_obj))
