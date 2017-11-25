#!/usr/bin/env pyton3

def adder(x, y):
    return x + y

str1 = "lalala spam"
str2 = "hehehe ham"

a = 1
b = 3.56

c = [ x * 2 for x in "eggs" ]
d = dict(enumerate(c))

print(adder(str1, str2))
#adder(a, str2) different types, strong type system
print(adder(a, b))
print(adder(a, a ** 3))
#adder(b, c) different types
print(adder(a, ord(c[0][0])))
print(adder(c, c[1:]))
#adder(d, { d[key] : key for key in d }) different types
#but:
d.update({ d[key] : key for key in d })
print(d)
