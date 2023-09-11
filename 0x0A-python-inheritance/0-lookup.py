#!/usr/bin/python3
"""
return the list of available attributes
and methods of the object.
"""

def lookup(obj):
    """return the list of the available attributes"""
    return dir(obj)
