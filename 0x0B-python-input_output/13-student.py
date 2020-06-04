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

    def to_json(self, attrs=None):
        """return attrs
        if its a list iterate and retrieve only
        specific values
        """
        if type(attrs) == list:
            new_dict = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    new_dict.update({k: v})
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes
        of the Student instance
        """
        for k, v in json.items():
            if hasattr(self, k):
                setattr(self, k, v)
