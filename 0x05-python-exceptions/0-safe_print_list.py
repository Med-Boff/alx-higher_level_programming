#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n_elements = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            n_elements += 1
    except IndexError:
        pass
    print()
    return n_elements
