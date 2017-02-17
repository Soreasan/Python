#!/usr/bin/env python3
# Kenneth Adair
# Demo of Lists while following along with Pluralsight's Python Fundamentals course.

#Create a list with a string
s = "show how to index into sequences".split()
print(s)
#We can index elements in the list with square brackets
print(s[4])
#Python also has the ability to index from the end with -1 being the last
#-1 is the first because -0 is still zero so negative indexing is 1 based
print(s[-1])
#Slicing lets us grab part of the list
print(s[1:4])
#To slice all elements but first and last we can do this:
print(s[1:-1])
#To slice all elements from the beginning up to but not including 3:
print(s[:3])
#To slice all elements from the third up to and including the end do:
print(s[3:])
#We can "slice" all the elements like this:
full_slice = s[:]
#It has a different identity but an equal value
#The references within the list are the same though
print(full_slice)
print(full_slice is s)
print(full_slice == s)
#There are other ways to construct a copy
#However each of these techniques forms a shallow copy
u = s.copy()
v = list(s)
print(v)
