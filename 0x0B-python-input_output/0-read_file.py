#!/usr/bin/python3
""" Module containing a function that reads from a file """


def read_file(filename=""):
    """ Function reading from a file

    Args:
        filename: filename

    Raises
        Exception: for when the file can be opened

    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_text = f.read()
        print(read_text, end='')
