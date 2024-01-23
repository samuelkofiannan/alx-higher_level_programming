#!/usr/bin/python3

import sys

""" A function that executes a function safely.
    Returns:
        The results of the function.
    Otherwise - None
"""

def safe_function(fct, *args):
    try:
        num = fct(*args)
        return num
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
