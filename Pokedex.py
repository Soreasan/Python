#!/usr/bin/env python3
# Kenneth Adair
# This script retrieves a pokemon's name based on the number the user inputs.
# Based on a Twitter retrieving script from Pluralsight's 
# "Raspberry Pi for Developers" course by Jon Flanders
# However my version uses a completely different api.
# The concepts are the same though
# This version tacks a very basic GUI onto the program

import tkinter
import http.client
import json

root = tkinter.Tk()
listbox = tkinter.Listbox(root)
text = tkinter.Entry(root)

def buttonclick():
    c = http.client.HTTPConnection('pokeapi.co')
    c.request('GET','/api/v2/pokemon/{0}/'.format(text.get()))
    r = c.getresponse()
    data = r.read()
    datas = str(data, 'utf-8')
    o = json.loads(datas)
    pokemon = o['name']
    listbox.delete(0, tkinter.END)
    listbox.insert(tkinter.END, pokemon)
    #listbox.insert(tkinter.END, 'test')
    
button = tkinter.Button(root, text="Enter a number \nbetween 1 and 811:", command=buttonclick)
button.pack(side="left")
text.pack(side="left")
listbox.pack(side="bottom", fill="both", expand=True)

root.mainloop()
