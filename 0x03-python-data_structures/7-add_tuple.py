#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = ()
    while len(tuple_a) < 2:
        tuple_a = tuple_a + (0,)
    while len(tuple_b) < 2:
        tuple_b = tuple_b + (0,)
    for x, y in zip(tuple_a, tuple_b):
        res = res + (x + y,)
    return res
