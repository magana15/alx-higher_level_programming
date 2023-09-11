#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Square(BaseGeometry):
    """
    A Square class shape, inheirts from BaseGeometry
    """
    def __init__(self, size):
        """"
        Init function for Square

        Attribute:
            size (int):size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        str function to print width/height

        Returns:
            Return width/height
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """
        A function to calculate the area of the Square
        """
        return self.__size ** 2
