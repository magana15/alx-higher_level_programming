#!/usr/bin/python3
""" class Square defining a square"""

class Square:
    """ class Square defining a square"""
    def __init__(self, size=0):
        """ init square

        Args:
            value (int): size of the square.
        """
        self.size = size

    @property
    def size(self):
        """int: private size.

        Returns:
            Private size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set value into size, must be int.

        Args:
            value (int): size of the square.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value  

    def area(self):
        """returns the area

        Returns:
            area
        """
        return self.__size**2
