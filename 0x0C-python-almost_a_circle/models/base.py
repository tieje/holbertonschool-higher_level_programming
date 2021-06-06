#!/usr/bin/python3
"""
Base class for almost a circle
"""
import json


class Base:
    """
    Base class for almost a circle
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json string repr of list_dictionaries"""
        result = json.dumps(list_dictionaries, default=lambda o: o.__dict__)
        if result == None or result == {}:
            return "[]"
        return str(result).replace('_Rectangle__', '')

    @staticmethod
    def from_json_string(json_string):
        """returns list from JSON string"""
        if json_string == None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json class data to file"""
        with open(cls.__name__ + '.json', mode='w') as file:
            if list_objs == None or list_objs == []:
                file.write('[]')
            else:
                result = []
                for i in list_objs:
                    json_string = Base.to_json_string(i).strip('[]')
                    result.append(json.loads(json_string))
                file.write(str(result))
    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
