#!/usr/bin/env python3

#We can create a list from a string using the split() method
w = "the quick brown fox jumps over the lazy dog".split()
print(w)
#We can search for a value like this which returns the index it's at
i = w.index('fox')
print(i)
print(w[i])
#w.index('unicorn') #Error
#You can check for membership with the 'in' and 'not in' keywords
print(37 in [1, 78, 9, 37, 34, 53])
print(78 not in [1, 78, 9, 37, 34, 53])
#Create a new list
u = "jackdaws love my big sphinx of quarts".split()
print(u)
#We can delete from a list by index
del u[3]
print(u)
#We can also delete from a list by value
u.remove('jackdaws')
print(u)
#Trying to delete an item that isn't there causes a ValueError
#u.remove('pyramid')
#New list...
a = "I accidentally the whole universe".split()
print(a)
#We can insert by index
a.insert(2, "destroyed")
print(a)
#we can combine the list into a word again using a space join operator
words = ' '.join(a)
print(words)
#You can concatenate a list with the following syntaxes:
m = [2, 1, 3]
print(m)
n = [4, 7, 11]
print(n)
k = m + n
print(k)
k += [18, 29, 47]
print(k)
k.extend([76, 129, 199])
print(k)
