#!/usr/bin/env python3
# Kenneth Adair
# Following along with Pluralsight's Python Fundamentals course.
# Demo of the Dictionary collection
# Dictionaries are delimited by { } and are key value pairs
urls = {'Google': 'http://google.com',
        'Pluralsight': 'http://pluralsight.com',
        'Sixty North': 'http://sixty-north.com',
        'Microsoft': 'http://microsoft.com'}
#We access the individual elements using their keys
print(urls['Pluralsight']) 
#Here is a list of tuples
names_and_ages = [('Alice', 32), ('Bob', 48), ('Charlie', 28), ('Daniel', 33)]
#Here we can cast the list of tuples to a dictionary
d = dict(names_and_ages)
print(d)
#We can also create a dictionary with the keyword dict
phonetic = dict(a='alfa', b='bravo', c='charlie', d='delta', e='echo', f='foxtrot')
print(phonetic)
#Here's another dictionary:
d = dict(goldenrod=0xDAA520, indigo=0x4B0082, seashell=0xFFF5EE)
print(d)
#We can copy it with the copy keyword
e = d.copy()
print(e)
#We can copy it with the dict constructor
f = dict(e)
print(f)
#Make an extra dictionary that we'll append to f
g = dict(wheat=0xF5DEB3, khaki=0xF0E68C, crimson=0xDC143C)
print(g)
# Use update to append the dictionaries
f.update(g)
print(f)
# If you try to use the update keyword but the keys are already in 
# the dictionary the target key values will be replaced/updated
stocks = {'GOOG':891, 'AAPL': 416, 'IBM':194}
print(stocks)
stocks.update({'GOOG':894, 'YHOO':25})
print(stocks)
# You can iterate through a dictionary but the order is random
for key in stocks:
    print("{key} => {value}".format(key=key, value=stocks[key]))
# We can also only iterate through the values with the values() keyword
for value in stocks.values():
    print(value)
# You can also iterate by keys but it's not used very often
# because default iteration is already by keys
for key in stocks.keys():
    print(key)
# You can also retrieve the pairs as tuples
for key, value in stocks.items():
    print("{key} => {value}".format(key=key, value=value))
#We can check for membership in a dictionary with the "in" and "not in"
# keywords, but it only works on the keys
print('GOOG' in stocks)
#We can use the del keyword to remove elements
print(stocks)
del stocks['YHOO']  #Oh no not Yahoo!
del stocks['IBM']   #Oh no not Big Blue!
print(stocks)

#We can make a dictionary over multiple lines:
m ={'H': [1, 2, 3],
    'He': [3, 4],
    'Li': [6, 7],
    'Be': [7, 9, 10],
    'B': [10, 11],
    'C': [11, 12, 13, 14]}
#We can append to a single item
m['H'] += [4, 5, 6, 7]
#The dictionary is mutable so we can add new items
m['N'] = [13, 14, 15]
#Pretty printing with pprint
from pprint import pprint as pp
pp(m) 
