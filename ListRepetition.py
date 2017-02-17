#!/usr/bin/env python3

#We can multiply a list with the * operator
c = [21, 37]
print(c)
d = c * 4
print(d)
#It's frequently used with zero to initialize an empty list
print([0] * 9)
#However reptition is shallow so it makes a bunch of pointers
#pointing to the same spot
s = [[-1, +1]]*5
print(s)
#If we append to one index we append to them all
s[3].append(7)
print(s)
