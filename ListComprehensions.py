#!/usr/bin/env python3
'''
Kenneth Adair
Taken from Python Fundamentals Course on Pluralsight
'''
words = "Why sometimes I have believed as many as six impossible things before breakfast".split()
# List Comprehension
# General format is [ expr(item) for item in iterable ]
lengths = [len(word) for word in words]
print(lengths)
