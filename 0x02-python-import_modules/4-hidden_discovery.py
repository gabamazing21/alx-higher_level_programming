#!/usr/bin/python3
import importlib.util
from hidden_4 import *
import os
if (__name__ == '__main__'):
    """
    current_directory = os.getcwd()
    spec = importlib.util.spec_from_file_location("hidden_4", f"{current_directory}/hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    """
    print(dir())

