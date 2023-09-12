#!/usr/bin/python3
""" 
Module that creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """ 
    
    Function that create an Object from JSON file

    Args:
        filename:filename name

    Raises:
        Exception: when the object not encoded

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
