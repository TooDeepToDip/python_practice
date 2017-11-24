#!/usr/bin/env python3

import math
init = [ 2, 4, 9, 16, 25]
l1 = []
for x in init:
    l1.append(math.sqrt(x))

l2 = list(map(math.sqrt, init))

l3 = [ math.sqrt(x) for x in init ]

l4 = [ x ** 0.5 for x in [ y * 2 if y == 1 else y ** 2 for y in range(1, 6)] ]

print(l1)
print(l2)
print(l3)
print(l4)
