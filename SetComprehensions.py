#!/usr/bin/env python3
# Demo from Pluralsight's Python Fundamentals Course of Set Comprehensions
from math import factorial
output = {len(str((factorial(x)))) for x in range(20)}
print(output)
