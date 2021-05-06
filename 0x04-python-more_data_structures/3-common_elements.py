#!/usr/bin/python3
def common_elements(set_1, set_2):
    def findinset1(x): return x in set_1
    filterobj = filter(findinset1, set_2)
    return filterobj
