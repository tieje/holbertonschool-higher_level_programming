#!/usr/bin/python3
"""
Base class for almost a circle
"""
import json
import csv

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
        if list_dictionaries == None or list_dictionaries == {}:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns list from JSON string"""
        if type(json_string) == dict:
            return json_string
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
                dictionaries = []
                for i in list_objs:
                    dictionaries.append(i.to_dictionary())
                file.write(Base.to_json_string(dictionaries))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Square':
            dummy = cls(2)
        elif cls.__name__ == 'Rectangle':
            dummy = cls(2, 2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        try:
            with open(cls.__name__ + '.json', mode='r') as file:
                content = cls.from_json_string(file.read())
                instances = []
                for i in content:
                    instances.append(cls.create(**i))
                return instances
        except FileNotFoundError:
            return []
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save data to csv file"""
        with open(cls.__name__ + '.csv', mode='w') as file:
            dictionaries = []
            field_names = []
            for i in list_objs:
                dictionaries.append(i.to_dictionary())
            for k, v in dictionaries[0].items():
                field_names.append(k)
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(dictionaries)

    @classmethod
    def load_from_file_csv(cls):
        """return a list of instances from a csv file"""
        try:
            with open(cls.__name__ + '.csv', mode='r') as file:
                instances = []
                reader = csv.DictReader(file)
                for row in reader:
                    instances.append(cls.create(**row))
                return instances
        except FileNotFoundError:
            return []
