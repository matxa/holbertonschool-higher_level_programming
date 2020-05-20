#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if int(size) >= 0:
            self.__size = size
    try:
        def area(self):
            return self.__size * self.__size
    except ValueError:
        print("size must be >= 0")
    except TypeError:
        print("size must be an integer")
