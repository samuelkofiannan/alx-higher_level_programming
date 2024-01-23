#!/usr/bin/python3

from __future__ import print_function
import sys

""" A function that executes a function safely.
    Returns:
        The results of the function.
    Otherwise - None
"""

def safe_function(fct, *args):
    try:
        num = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return num
