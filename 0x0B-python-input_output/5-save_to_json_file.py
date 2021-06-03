#!/usr/bin/python3
"""Writes an Object to a text file using JSON repr"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, mode='w', encoding='utf_8') as file:
        json.dump(my_obj, file)
