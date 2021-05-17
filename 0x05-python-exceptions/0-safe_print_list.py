#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real_print = 0
    for i in range(x):
        try:
            print(my_list[i], end='')
            real_print += 1
        except:
            break
    print('', end='\n')
    return real_print
