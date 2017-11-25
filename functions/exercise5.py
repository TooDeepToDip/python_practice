#!/usr/bin/env python3

def copyDict(dict):
    return { key : dict[key] for key in dict }

d = { 'a': 5 , 'b': 6, 'c': 7 }
d2 = copyDict(d)
print(d2)
d2.clear()
print(d2)
print(d)
