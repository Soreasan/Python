# Kenneth Adair
# A fun, super basic python program I did for fun

import random

def calculate_winner(playerChoice, computerChoice):
    #Check for invalid input
    if playerChoice != "rock" and playerChoice != "scissors" and playerChoice != "paper":
         print("Invalid input")
    #Check for ties
    if playerChoice == computerChoice:
        print("You both picked ", playerChoice, ", you tied!")
    if playerChoice == "rock":
        if computerChoice == "scissors":
            print("You picked rock and the computer picked scissors, YOU WIN!")
        else:
            print("You picked rock and the computer picked scissors, YOU LOSE!")
    elif playerChoice == "scissors":
        if computerChoice == "paper":
            print("You picked scissors and the computer picked paper, YOU WIN!")
        else:
            print("You picked scissors and the computer picked rock, YOU LOSE!")
    elif playerChoice == "paper":
        if computerChoice == "rock":
            print("You picked paper and the computer picked rock, YOU WIN!")
        else:
            print("You picked paper and the computer picked scissors, YOU LOSE!")

def play_game():
    computerChoice = "scissors"
    rand = random.choice([1, 2, 3])
    if(rand == 1):
        computerChoice = "rock"
    if(rand == 2):
        computerChoice = "paper"
    print("Let's play Rock Paper Scissors!")
    print("Type 'rock' for Rock, 'paper' for paper, 'scissors' for scissors")
    playerChoice = input()
    calculate_winner(playerChoice, computerChoice)

keepGoing = True

while keepGoing:
    play_game()
    print("Would you like to play again?  y for yes, no for no")
    if input() != "y":
        keepGoing = False  
