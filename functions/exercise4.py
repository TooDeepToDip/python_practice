#!/usr/bin/env pyton3

def adder(good = 1, bad = 2, ugly = 100):
    return good + bad + ugly

import functools
def adder2(*args, **kargs):
    return functools.reduce(lambda x,y: x + y, (kargs[key] for key in kargs))

str1 = "lalala spam"
str2 = "hehehe ham"

a = 1
b = 3.56

c = [ x * 2 for x in "eggs" ]
d = dict(enumerate(c))

print(adder(str1, str2, str1[2:5]))
print(adder(a, b))
#print(adder(a, a, 3.14, ugly = 4)) got multiple values for argument 'ugly'
#print(adder(str1))
print(adder(ugly = 3, good = 3))

#print(adder2(str1, str2, str1[2:5])) list of named parameters is empty
#print(adder2(a, b)) again
#print(adder(a, a, 3.14, ugly = 4)) got multiple values for argument 'ugly'
#print(adder(str1))
print(adder2(ugly = 3, good = 3))
print(adder2(ugly = str1, good = str2, bad = str1[2:5]))
