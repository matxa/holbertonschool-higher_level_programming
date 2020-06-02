#!/usr/bin/python3
"""Empty BaseGeometry class"""


class BaseGeometry:
    """Define class"""
    def area(self):
        """raise Exception Error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
