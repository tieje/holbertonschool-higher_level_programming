#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    def mult2(x): return (x[0], x[1] * 2)
    new_dict = dict(map(mult2, a_dictionary.items()))
    return new_dict
