#!/usr/bin/python3
# Kenneth Adair
# This script retrieves a pokemon's name based on the number the user inputs.
# Based on a Twitter retrieving script from Pluralsight's 
# "Raspberry Pi for Developers" course by Jon Flanders
# However my version uses a completely different api.
# The concepts are the same though

import http.client
import json

user_input = input("Input a number between 1 and 811:")

c = http.client.HTTPConnection('pokeapi.co')
getRequest = '/api/v2/pokemon/'
getRequest += user_input
getRequest += '/'
c.request('GET', getRequest)
r = c.getresponse()
data = r.read()
datas = str(data, 'utf-8')
o = json.loads(datas)
pokemon = o['name']
print(pokemon)
