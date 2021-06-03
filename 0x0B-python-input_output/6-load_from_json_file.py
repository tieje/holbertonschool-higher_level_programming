#!/usr/bin/python3
"""Create an Object from a JSON file"""
import json


def load_from_json_file(filename):
    with open(filename) as file:
        return json.load(file)
