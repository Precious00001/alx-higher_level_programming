#!/usr/bin/python3
"""Square Module """


class Square:
    """ The "Square" class is defined as a geometric shape.

        Attributes:
            size (int): Square dimension
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): Length of one side of the square.

        Returns:
            None
        """
        self.size = size

    def area(self):
        """
        set square square area

        Return:
            the current square area (int)
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        getter of size

        Return:
            Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of size

        Args:
            size (int): Length of one side of the square.
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
                raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        prints  a square of a specified size using the character sequence "##".

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for x in range(self.size):
                    print("#" * self.size)
