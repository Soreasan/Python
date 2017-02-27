#!/usr/bin/env python3
# Kenneth Adair
# Following along with Pluralsight's Python Fundamentals course.
# Demo of Sets

# Create a set with curly braces
p = {6, 28, 496, 8128, 33550336}
print(p)
print(type(p))
#If we use empty curly braces it's a dictionary though
d = {}
print(type(d))
#Create an empty set with a constructor "set()"
e = set()
print(type(e))
#You can use a set constructor to turn a list into a set that removes duplicates
s = set([2, 4, 16, 64, 4096, 65535, 262144])
t = {1, 4, 2, 1, 7, 9, 9}
print(t)
#You can iterate through a set but the order is random
for x in {1, 2, 4, 8, 16, 32}:
    print(x)
#you can check if something is in a set with the "in" and "not in" operator
print(2 in t)
print(2 not in t)
#To add a single value to a set use the add method
print(t)
t.add(10)
print(t)
#Adding an element that already exists does nothing
t.add(10)
t.add(10)
print(10)
#You can add as many elements as you'd like using UPDATE including a set
t.update([11, 12, 13])
#If you use the remove method and the item isn't available you get an error
t.remove(11)
#t.remove(11)
#But if you use discard and it's not there you won't get an error
t.discard(11)
print(t)
#You can use the copy constructor or set constructor to make a shallow copy
j = t.copy
print(j)
m = set(t)
print(m)

# A useful aspect of sets is calculating set unions, set differences, subsets, etc
#Various sets
blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

#Union gets everything that is in either or both sets
print(blue_eyes.union(blond_hair))
#Intersection gets the elements that are present in both sets
print(blue_eyes.intersection(blond_hair))
#Difference let's you identify which people are in one set but not the other
#This specifically displays everything in the first set(blond_hair) that's
#not in the second set(blue_eyes)
print(blond_hair.difference(blue_eyes))
#Symmetric difference displays everything that is in one set or the
#other but not both.  (Think XOR/Exclusive OR)
print(blond_hair.symmetric_difference(blue_eyes))
#Subset let's us see if one set is a subset of another, returns true/false
print(smell_hcn.issubset(blond_hair))
#Superset let's us see if one set is a superset of another, returns true/false
print(taste_ptc.issuperset(smell_hcn))
#To see if two methods have nothing in common use isdisjoint
print(a_blood.isdisjoint(o_blood))
