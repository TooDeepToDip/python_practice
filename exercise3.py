#!/usr/bin/env pyton3

import functools

def adder(*args):
    return functools.reduce(lambda x, y: x + y, args)

def adder2(*args):
    sum = args[0]
    for arg in args[1:]:
        sum += arg
    return sum

str1 = "lalala spam"
str2 = "hehehe ham"
str3 = "gagaga eggs"

a = 1
b = 3.56
e = 1000

c = [ x * 2 for x in "eggs" ]
d = dict(enumerate(c))

print("--->adder1:")
print(adder(str1, str2, str3))
#adder(a, str2) different types, strong type system
print(adder(a, b, e))
print(adder(a))
#adder(b, c) different types
print(adder(a, ord(c[0][0]), ord(c[0][1])))
print(adder(c, c[1:], c[0:1]))
#adder() throws typeError!
#adder(d, { d[key] : key for key in d }) different types
#but:
d.update({ d[key] : key for key in d })
print(d)

print("--->adder2:")
print(adder2(str1, str2, str3))
print(adder2(a, b, e))
print(adder2(a))
print(adder2(a, ord(c[0][0]), ord(c[0][1])))
print(adder2(c, c[1:], c[0:1]))
#adder2() throws typeError!
