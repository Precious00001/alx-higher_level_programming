#!/usr/bin/python3
"""
Contains the "append after" function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert text after each line that contains
    a specific string in a file..

    Args:
        filename (str): The name of the file.
        new_string (str): The string to insert.
    """
    with open(filename, "r+", encoding="utf-8") as f:
        w = ""
        for line in f:
            w += line
            if search_string in line:
                w += new_string
        f.seek(0)
        f.write(w)
