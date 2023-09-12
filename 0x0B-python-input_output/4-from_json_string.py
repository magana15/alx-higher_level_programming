#!/usr/bin/python3
""" 
Module that contains a function that return an object by
a JSON representation.
"""
import json


def from_json_string(my_str):
    """ Function that return an object by JSON representation

    Args:
        my_str: JSON representation

    Raise:
        Exception: when not decoded

    """
    return json.loads(my_str)
