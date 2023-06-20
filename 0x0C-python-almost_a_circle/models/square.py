#!/usr/bin/python3
"""
Defines a square class
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
        Represent a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @size.setter
    def size(self, value):

        self.height = value
        self.width = value

    def __str__(self):
        """informal string representation of the square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
        """
        p = 0
        if args:
            for arg in args:
                if p == 0:
                    self.id = arg
                if p == 1:
                    self.size = arg
                if p == 2:
                    self.x = arg
                if p == 3:
                    self.y = arg
                p += 1
        else:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))

    def to_dictionary(self):
        """
            Return the dictionary
            representation of the Square.
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    @property
    def size(self):
        """
            Get/set the size of the Square.
        """
        return self.width
