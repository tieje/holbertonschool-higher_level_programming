#!/usr/bin/python3
import json
"""Return an object represented by a JSON string"""


def from_json_string(my_str):
    """Return an object represented by a JSON string"""
    return json.loads(my_str)
