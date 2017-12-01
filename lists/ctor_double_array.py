#!/usr/bin/env python3
# make list:
# [ [1, 2, 3]
#   [4, 5, 6]
#   [7, 8, 9] ]

# get list of iterators
args = [ iter(range(1, 10)) ] * 3
# repack to tuple of values from iterators,
# then convert tuples to lists
l = [ list(t) for t in list(zip(*args)) ]
