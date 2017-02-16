#!/usr/bin/env python3

#This create a range from 0 to 4
print(range(5))
#Range is frequently used with FOR loops
for i in range(5):
    print(i)
#We can also create a range with a start and end value
print(range(5, 10))
#We can create a list of each item by wrapping it with a list constructor
a = list(range(5, 10))
print(a)
#We can also create a list with an option third step value
b = list(range(0, 10, 2))
print(b)
#Here's the bad way of iterating through a list that's "unpythonic"
s = [0, 1, 4, 6, 13]
for i in range(len(s)):
    print(s[i])
#Here's a better way of iterating through a list that's "pythonic"
for v in s:
    print(v)
#If for some reason you need a counter while iterating use the enumerate() function
#enumerate() returns tuples
t = [6, 372, 8862, 148800, 2096886]
for p in enumerate(t):
    print(p)
# We can use tuple unpacking so we don't have to deal with the tuple
for i, v in enumerate(t):
    print("i = {}, v = {}".format(i, v))
