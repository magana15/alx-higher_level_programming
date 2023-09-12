#!/usr/bin/python3
""" 
Module that writes an Object to a text file using
a JSON representation
"""
import json

def save_to_json_file(my_obj, filename):
    """ 
    Function that write an object to a text file
    by a JSON representation.

    Args:
        my_obj: object
        filename: textfile name

    Raise:
        Exceptions: when the object not encoded
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
