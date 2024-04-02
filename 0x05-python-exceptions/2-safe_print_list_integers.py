#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    real_n = 0

    for n_elements in range(x):
        try:
            print("{:d}".format(my_list[n_elements]), end='')
            real_n += 1
        except (ValueError, TypeError):
            pass
    print()
    return real_n
