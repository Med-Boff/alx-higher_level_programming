#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        division_v = a / b
    except (ValueError, TypeError, ZeroDivisionError):
        division_v = None
    finally:
        print("Inside result: {}".format(division_v))
    return division_v
