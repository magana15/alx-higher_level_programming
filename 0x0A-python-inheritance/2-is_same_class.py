#!/usr/bin/python3
"""
return True if the object is exactly an instance of the specified class
; otherwise return False.
"""

def is_same_class(obj, a_class):
    """
    return True if the object is exactly an instance
    """
    return True if type(obj) == a_class else False
