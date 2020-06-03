#!/usr/bin/python3
"""A class that defines a student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name,
        last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dictionary
        representation
        """
        return self.__dict__
