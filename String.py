#!/usr/bin/env python3
# Kenneth Adair
# Following along with Python Fundamentals course.
# This is a demo of strings in Python

#To determine the length of a string we can use the length function
print(len("Hello World!"))
#We can concatenate strings using the plus operator!
s = "Hello"
s += " World!"
print(s)
#We can also concatenate strings using the .join method
colors = ';'.join(['#45ff23', '#2321fa', '#1298a3', '#a32312'])
print(colors)
#We can split them up using the split method
print(colors.split(';'))
#We can combine strings using the empty string
highwayman = ''.join(['high', 'way', 'man'])
print(highwayman)
#To seperate a string we can use partition to create a tuple from a string
unforgettableTuple = "unforgetable".partition("forget")
print(unforgettableTuple)
#Instead of assigning the results to a tuple we can get the three values
departure, seperator, arrival = "London:Edinburgh".partition(':')
print(departure)
print(arrival)
#Alternatively a common practice is to use "_" for dummy values
origin, _, destination = "London:Edinburgh".partition(':')
print(origin)
print(destination)
#We can use the .format() function to mimic printf in C
stringVar = "The age of {0} is {1}. {0}'s birthday is on {2}".format('Fred', 24, 'October 31')
print(stringVar)
#Alternatively we can ignore the number if we put the arguments in order
print("Reticulating spline {} of {}.".format(4, 23))
#We can also assign the values by name
print("Current position {latitude} {longitude}".format(
    latitude="60N", longitude="5E"))
#We can also print the contents of a tuple in the string
pos = (65.2, 23.1, 82.2)
print("Galactic position x={pos[0]} y={pos[1]} x={pos[2]}".format(pos=pos))
