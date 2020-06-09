#!/usr/bin/python3
"""class that defines Base"""
import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """if id is not None, assign public instance id to id
        otherwise increment the __nb_objects and set id equal
        to Base.__nb_objects
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json representation
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        ls_dict = json.dumps(list_dictionaries)
        return ls_dict

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file
        """
        list_t = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write(str(list_t))
            else:
                for i in list_objs:
                    list_t.append(cls.to_dictionary(i))
                file.write(cls.to_json_string(list_t))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON
        string representation json_string
        """
        if not json_string or len(json_string) == 0:
            return []
        data = json.loads(json_string)
        return data

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with
        all attributes already set
        """
        temp_obj_repr = cls(1, 1)
        if dictionary:
            temp_obj_repr.update(**dictionary)
        return temp_obj_repr

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            ls_ap = []
            with open(filename) as file:
                my_str = file.read()
                data = cls.from_json_string(my_str)
                for i in data:
                    ls_ap.append(cls.create(**i))
            return ls_ap
        except FileNotFoundError:
            return []
