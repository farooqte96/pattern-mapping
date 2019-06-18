"""
This script applies the required formating rules on given string
"""
from . import modify_string

def apply_format(string, integers):
    """This function is used to apply formating rules."""
    result = []
    for integer in integers:
        new_string = modify_string.modify_string(string, integer)
        result.append(new_string)
    return result
