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
