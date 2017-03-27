#!/usr/bin/env python3
# Kenneth Adair
# Taken from Python Fundamentals course on Pluralsight
import sys

# A module for demonstrating exceptions.
def convert(s):
    # Convert an integer
    try:
        x = int(s)
        print("Conversion succeeded! x = ", x)
    except ValueError:
        print("ValueError")
        print(s)
        x = -1
    except TypeError:
        print("TypeError")
        print(s)
        x = -1
    return x

def convert2(s):
    try: 
        return int(s)
    except(ValueError, TypeError) as e:
        print("Conversion error: {}"\
            .format(str(e)),
            file = sys.stderr)
        return -1

main1():
    v = convert(10.5)
    y = convert("error!")
    my_list = [(2, 1), (3, 4)]
    y = convert(my_list)

main2():
    print(convert2(12.5))
    print(convert("error!")
    print(convert([(2, 1), (3, 4)]))

main2()


