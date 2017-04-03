#!/usr/bin/env python3
#Taken from Python Fundamentals course on Pluralsight
from pprint import pprint as pp

country_to_capital  =  {'United Kingdom': 'London',
                        'Brazil': 'Brazilia',
                        'Morocco': 'Rabat',
                        'Sweden': 'Stockholm'}

# {key_expr: value_expr for item in iterable }
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
pp(capital_to_country)

# Duplicates: later keys overwrite earlier keys
words = ["hi", "hello", "foxtrot", "hotel"]
letter_words = {x[0]: x for x in words }
print(letter_words)
