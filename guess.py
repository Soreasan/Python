# Kenneth Adair
# Following a long with example in "Learning to Program Part 2 - Introduction to Python"
# In Pluralsight by Scott Allen
# Made with Idle, Python 3.5
# This is a GUESS A NUMBER game

import random

print("Hello, what is your favorite number?")

# input asks user for input and then the user hits enter
number = input()


minNumber = 1
maxNumber = 100
magicNumber = random.randint(minNumber, maxNumber)
message = "The magic number is between {0} and {1}"
print(message.format(minNumber, maxNumber))
# IS the guess right?
found = False


while not found:
    print("Guess what it is?")
    #input() treats everything as a string by default
    guess = int(input())
    if guess == magicNumber:
        found = True
        print("***")
    if guess < magicNumber:
        print("Too low")
    if guess > magicNumber:
        print("Too high")
        
print("You got it")
