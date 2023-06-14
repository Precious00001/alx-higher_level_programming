#!/usr/bin/python3
"""
The string representation of an object in JSON format.
"""

import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
