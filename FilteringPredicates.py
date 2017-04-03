#!/usr/bin/env python3
# Demo of filtering predicates from Python Fundamentals course on Pluralsight
from math import sqrt

# Simple method to test for primeness
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# [expr(item) for item in iterable if predicate(item)]
primes = [x for x in range(101) if is_prime(x)]
print(primes)
