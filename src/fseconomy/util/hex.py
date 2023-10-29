"""
fseconomy.util.hex
~~~~~~~~~~~~~~~~~~

This module contains a set of hex helper functions.
"""


def is_hex(value: str) -> bool:
    """validate if a string represents a number in hexadecimal format

    :param value: string to validate
    :return: True if string represents a hexadecimal number, otherwise False
    """
    try:
        _ = int(value, 16)
        return True
    except ValueError:
        return False
