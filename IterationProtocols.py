#!/usr/bin/env python3
# Demo of Iteration protocols from Python Fundamentals on Pluralsight

iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
#Create an iterator
iterator = iter(iterable)
#The next keyword moves the iterator to the next element in the collection
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
