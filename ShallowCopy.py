#!/usr/bin/env python3
print("Hello World!")
#Create a list
a = [[1, 2], [3, 4]]
print(a)
#Create a copy
b = a[:]
print(b)
#The pointers to the two lists are different but the values in the lists
#Are pointing to the exact same boxes!
print("b is a ", b is a)
print("a == b ", b == a)
#a and b point to the same inner list objects
print("a[0] is b[0] ", a[0] is b[0])
#If we change a[0] it will update the pointer and get new values
a[0] = [8, 9]
print(a[0])
print(b[0])
#If we append to a[1] it affects b[1] too since they point to same area
a[1].append(5)
print(a[1])
print(b[1])
print(a)
print(b)
