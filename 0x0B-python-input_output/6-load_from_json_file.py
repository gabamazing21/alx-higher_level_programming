#!/usr/bin/python3
""" This module provide functions to read json object from a file"""
import json


def load_from_json_file(filename):
    """ this function read json from file"""
    with open(filename, 'r', encoding="UTF-8") as f:
        return json.loads(f.read())
