#!/usr/bin/python3
"""Square class"""


class Square:
    """Class Square defines a square.

    Attributes:
        size: size of the Square
        positon: printing
    """
    def __init__(self, size=0, position=(0, 0)):
        """Instation of size and positon
        Args:
            size: Attribute
            position: Attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        """Method for calc the area of square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """property to get size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """property to set size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """property to get position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """property to set position
        """
        if not isinstance(value, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """print ___squares
        """
        if self.__size == 0:
            print("")
        else:
            for a in range(self.__position[1]):
                print("")
            for b in range(self.__size):
                for b1 in range(self.__position[0]):
                    print(" ", end="")
                for b2 in range(self.__size - 1):
                    print("#", end="")
                print("#")
