#!/usr/bin/env python3
# Kenneth Adair
# Following along with Pluralsight's Python Fundamentals course.
# Demo of reversing and sorting lists.
#Make a list
g = [1, 11, 21, 1211, 112111]
print(g)
#Reverse a list
g.reverse()
print(g)
#Make another list
d = [5, 17, 41, 29, 71, 149, 3299, 7, 13, 67]
print(d)
#Sort the list
d.sort()
print(d)
#Sort the list in reversed/descending order
d.sort(reverse=True)
print(d)
#Another list
h = 'not perplexing do handwriting family where I illegibly know doctors'.split()
print(h)
#We can also sort by a criteria with the "key" keyword
h.sort(key=len)
print(h)
#We can join them back together like this:
print(' '.join(h))

