#!/usr/bin/env python3

def isPrime(y):
    x = y // 2
    while x > 1:
        if y % x == 0:
            print(y, 'has factor', x)
            break
        x = x-1
    else:
        print(y, 'is prime')

isPrime(13)
isPrime(13.0)
isPrime(15)
isPrime(15.0)
