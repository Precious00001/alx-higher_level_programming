#!/usr/bin/python3
"""
module inherit list
"""


class MyList(list):
    """MyList"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
