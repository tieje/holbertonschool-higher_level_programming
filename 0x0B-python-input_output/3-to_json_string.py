#!/usr/bin/python3
"""Returns json repr of an object(string)"""
import json


def to_json_string(my_obj):
    """Returns json repr of an object"""
    return json.dumps(my_obj)
