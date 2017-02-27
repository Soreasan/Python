#!/usr/bin/env python3
# Kenneth Adair
# Demo of Collection Protocols
# Following along with Pluralsight's Python Fundamentals course.
myList = [1, 2, 3]
print(type(myList))
#You can check for membership with the in and not in protocols
print(2.in(myList))
print(2 in myList)
print(2 not in myList)
#You can check the size with the len(s) function
print(len(myList))
#Can produce an iterator with iter(s)
for item in myList:
    print(item)
#Sequence protocols allow us to retrieve elements by index
print(myList[2])
# We can also find items by value
print("index of 3 is: ", myList.index(3))
#We can count items with count
print("We have ", myList.count(3) ," 3's")
#We can reverse a list with this:
for i in reversed(myList):
    print(i)
