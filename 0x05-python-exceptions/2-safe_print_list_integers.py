#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    real_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            real_printed += 1
        except ValueError:
            pass
        except TypeError:
            pass
    print('', end='\n')
    return real_printed
