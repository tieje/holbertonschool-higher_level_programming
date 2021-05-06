#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    def findinset1(x): return x not in set_1
    def findinset2(x): return x not in set_2
    filterobj1 = list(filter(findinset1, set_2))
    filterobj2 = list(filter(findinset2, set_1))
    new_set = filterobj1 + filterobj2
    return new_set
