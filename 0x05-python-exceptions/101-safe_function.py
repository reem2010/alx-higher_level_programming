#!/usr/bin/python3

import sys
def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as msg:
        result = None
        print("Exception: {}".format(msg), file=sys.stderr)
    finally:
        return (result)

