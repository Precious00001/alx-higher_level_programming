#!/usr/bin/python3
"""
Defines a JSON file-writing function.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an object to a text file by
    using a JSON representation.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
