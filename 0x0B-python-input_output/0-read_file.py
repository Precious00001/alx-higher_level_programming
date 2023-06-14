#!/usr/bin/python3
"""
A function that reads a UTF-8 encoded text file
and displays its content on the standard output (stdout).
"""


def read_file(filename=""):
    """
    A function that reads a UTF-8 encoded text file
    and outputs its contents to the standard output (stdout).
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
