#!/usr/bin/python3
"""import class Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Define Function"""
    def __init__(self, size):
        """validating size
        and Instantiating size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculating the area
        of a square
        """
        return self.__size * self.__size
