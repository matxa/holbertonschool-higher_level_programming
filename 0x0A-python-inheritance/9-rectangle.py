#!/usr/bin/python3
"""import class BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Define class"""
    def __init__(self, width, height):
        """width and height must be private. No getter or setter
        width and height must be positive integers,
        validated by integer_validator
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the erea
        of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
