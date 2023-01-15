"""Base Module"""


import json


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
        if list_objs is None or len(list_objs) == 0:
            f = open(f"{cls.__name__}.json", 'w')
            f.close()
            return
        with open(f"{cls.__name__}.json", 'w') as f:
            f.write(Base.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]))
