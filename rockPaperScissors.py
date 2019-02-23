#creating rock paper scissor game

#printing instructions
from random import *





#Define the computer functions
def rps():
    computer_choice = random.randrange(1,3):
    if computer_choice == 1:
        computer_choice_rock()
    elif computer_choice == 2:
        computer_choice_paper()
    else: 
        computer_choice_scissors()

# Define function when computer chooses rock

def computer_choice_rock():
    user_choice = raw_input("rock for Rock, paper for Paper, scissors for Scissors: ")
    if user_choice == "rock":
        print "You Tie. Computer and you both have choosen rock."
        try_again()
    if user_choice == "paper":
        print "You win. You choose paper and the computer choose Rock."
        try_again()
    if user_choice == "scissors":
        print "You loose. You choose scissors and the computer chooses rock."
        try_again()
    else:
        print "try again"
        computer_choice_rock()

# Define a function when a computer chooses paper

def computer_choice_paper():
    user_choice = raw_input("rock for Rock, paper for Papaer,scissors for Scissors:")
    if user_choice == "rock" or user_choice == "Rock" or user_choice == "ROCK":
        print "You Loose. Computer chooses paper and you have choosen rock."
        try_again()
    if user_choice == "paper " or user_choice == "Paper" or user_choice == "PAPER":
        print "Its a tie. You and computer both choose paper."
        try_again()
    if user_choice == "scissors" or user_choice == "Scissors" or user_choice == "SCISSORS":
        print "You Win. You choose scissors and the computer chooses paper."
        try_again()
    else:
        print "try again"
        computer_choice_paper()

# Define a function when computer chooses scissors

def computer_choice_scissors():
    user_choice = raw_input("rock for Rock, paper for Paper, scissors for Scissors:")
    if user_choice == "rock" or user_choice == "Rock" or user_choice == "ROCK":
        print "You win. you choose rock and the computer have chooses scissors."
        try_again()
    if user_choice == "paper" or user_choice == "Paper" or user_choice == "PAPER":
        print "You loose. You choose paper and the computer choose Scissors."
        try_again()
    if user_choice == "scissors" or user_choice == "Scissors" or user_choice == "SCISSORS":
        print "Its a tie. You choose scissors and the computer also choose scissors."
        try_again()
    else:
        print "try again"
        computer_choice_scissors()

#Define try again function

def try_again():
    choice = raw_input("Would you like to play again? (y/n)")
    if choice == "yes" or choice == "y" or choice == "Y":
        rps()
    elif choice == "n" or choice == "no" or choice == "N":
        print "Thanks for playing"
        quit()
    else:
        print "Try again"
        try_again()

rps()






