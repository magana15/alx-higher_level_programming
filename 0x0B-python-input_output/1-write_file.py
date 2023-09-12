#!/usr/bin/python3
""" 
Module that contains a function which writes to a txt file
"""


def write_file(filename="", text=""):
    """ Function that writes to a text file

    Args:
        filename:filename
        text:text to write

    Raises
        Exception: when to be opened

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
