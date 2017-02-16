#!/usr/bin/env python3

def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("Hello World!")
