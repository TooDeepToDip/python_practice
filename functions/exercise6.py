#!/usr/bin/env pyton3

def addDict(dict1, dict2):
    if type(dict1) != type(dict2): return None
    if type(dict1) == type(list()): return dict1 + dict2
    newDict = { key: dict1[key] for key in dict1 }
    for key in dict2:
        newDict[key] = dict2[key] 
    return newDict

d = { 'a': 5 , 'b': 6, 'c': 7 }
e = { 'm': 15 , 'b': 16, 'o': 17 }

f = addDict(d, e)
print(d)
print(e)
print(f)

k = [ 1, 2, 3, 4]
l = [ 5, 6, 7, 8]

m = addDict(k, l)
print(k)
print(l)
print(m)

