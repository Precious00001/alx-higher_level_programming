#!/usr/bin/python3
"""
A Student class that defines a Studen (module)
"""


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation
            of a Student instance"""
        return self.__dict__