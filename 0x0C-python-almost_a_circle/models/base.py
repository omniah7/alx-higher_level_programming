#!/usr/bin/python3
"""Base Module"""


import json
import csv


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """base constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries"""
        if (list_dictionaries is None
                or len(list_dictionaries) == 0):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file"""
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open(f"{cls.__name__}.json", 'w') as f:
            f.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string
        representation json_string"""
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""
        if dictionary is None or dictionary == {}:
            return
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        try:
            with open(f"{cls.__name__}.json", 'r') as f:
                ls = cls.from_json_string(f.read())
                return [cls.create(**obj) for obj in ls]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the csv string representation
        of list_objs to a file"""
        with open(f"{cls.__name__}.csv", 'w') as f:
            if list_objs is None or list_objs == []:
                f.write('[]')
                return
            if cls.__name__ == 'Rectangle':
                keys = ['id', 'width', 'height', 'x', 'y']
            else:
                keys = ['id', 'size', 'x', 'y']
            w = csv.DictWriter(f, fieldnames=keys)
            w.writerows([obj.to_dictionary() for obj in list_objs])

    @classmethod
    def load_from_file_csv(cls):
        """ returns a list of instances"""
        try:
            with open(f"{cls.__name__}.csv", 'r') as f:
                if cls.__name__ == 'Rectangle':
                    keys = ['id', 'width', 'height', 'x', 'y']
                else:
                    keys = ['id', 'size', 'x', 'y']
                ls = csv.DictReader(f, fieldnames=keys)
                ls = [dict([k, int(v)] for k, v in d.items()) for d in ls]
                return [cls.create(**obj) for obj in ls]
        except IOError:
            return []
