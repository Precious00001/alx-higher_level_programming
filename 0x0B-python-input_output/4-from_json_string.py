#!/usr/bin/python3
"""
contains the json str function
"""

import json


def from_json_string(my_str):
    """This function returns an object (a Python data structure)
    that is represented by a JSON string."""
    return json.loads(my_str)
