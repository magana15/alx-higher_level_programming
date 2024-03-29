#!/usr/bin/python3
"""Defines a function inherits_from()"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited,
     from the specified class ; otherwise False.

    Args:
        obj (a_class): object to check type.
        a_class (type): type of type to check.

    Return
        boolean: True or False..
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
