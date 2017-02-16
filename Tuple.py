#!/usr/bin/env python3
# Kenneth Adair
# Tuple demo
# Following along with Pluralsight's Python Fundamentals course.

#This is a tuple witha  string, a float, and an int
t = ("Norway", 4.953, 3)
#See the entire tuple
print(t)
#We can access specific elements of a tuple using square brackets
print(t[0])
print(t[2])
#We can determine the number of elements in a tuple using length
print(len(t))
#We can iterate over tuples using a FOR loop.
for item in t:
    print(item)
#We can print the repeated contents of tuples with the * operator
print(t * 3)
#We can concatenate tuples using the plus operator
t += (338186.0, 265e9)
print(t)
#Tuples can hold anything we want
a = ((220, 284), (1184, 1210), (2610, 2924), (5020, 5564))
#We can access these with the square bracket notation
print(a[2])
#We can access the individual contents by using multiple brackets
print(a[2][1])
#We can't create a single tuple with this notation:
h = (391)
print(h)
#it's the wrong type, it's an integer instead of a tuple
print(type(h))
# To properly create a single tuple use this syntax
k = (391,)
print(k)
#This is the right type, it's a tuple!
print(type(k))
#To create an empty tuple we just use this syntax:
e = ()
print(type(e))
#We can omit the parenthesis of tuples sometimes
p = 1, 1, 1, 4, 6, 19
print(p)
print(type(p))

#We can return the a tuple like this
def minmax(items):
    return min(items), max(items)

#We returned a tuple here
test = minmax([33, 55, 77, 88])
print(test)

#Alternatively we can return two seperate values
lower, upper = minmax([83, 33, 84, 32, 85, 31, 86])
print(lower, " ", upper)

#We can also assign variables in tuples in a weird way like this:
(a, (b, (c, d))) = (4, (3, (2, 1)))
print(a)
print(b)
print(c)
print(d)
#We can easily trade values like this:
a = 'jelly'
b = 'bean'
a, b = b, a
print(a, " ", b)
#If we want to create a tuple out of a list we can use a tuple constructor
print(tuple([561, 1105, 1729, 2465]))
#We can create a tuple out of a string
print(tuple("Carmichael"))
#We can check if a tuple contains something with the "in" operator
print(5 in (3, 5, 17, 257, 65537))
#We can check if a tuple doesn't contain something with the "not in" operator
print(5 not in (3, 5, 17, 257, 65537))
