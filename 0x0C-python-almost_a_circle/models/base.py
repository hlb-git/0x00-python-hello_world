#!/usr/bin/python3
"""base class for all other classes"""


import json


class Base:
    """id creation module"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__ + '.json', mode="w", encoding="UTF-8") as file:
            if not list_objs:
                file.write('[]')
            else:
                    data = cls.to_json_string([i.to_dictionary() for i in list_objs])
                    file.write(data)

    @staticmethod
    def from_json_string(json_string):
        """convert json back to data structure"""
        return json.loads(json_string or '[]')

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy_instance = cls(1)
        if dummy_instance:
            dummy_instance = (dummy_instance.update(**dictionary))
            return dummy_instance
        
    @classmethod
    def save_to_file_csv(cls, list_objs):
        import csv
        try:
            csv_list = [i.to_dictionary() for i in list_objs]
        except Exception:
            csv_list = '[]'
        keys = csv_list[0].keys()
        with open(cls.__name__ + '.csv', mode="w") as file:
            writer = csv.DictWriter(file, keys)
            writer.writeheader()
            writer.writerows(csv_list)
