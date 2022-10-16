from random import *

human_input = input("Type rock/paper/scissors or r/p/s: ")

computer = choice(["rock", "paper", "scissors"])

print(f"Computer chose {computer}!")
if human_input == 'rock' or "r":
    if computer == 'rock':
        print('It\'s a tie. Try again!')
    if computer == 'paper':
        print("Computer wins!")
    if computer == "scissors":
        print("Human wins!")

if human_input == 'paper' or "p":
    if computer == 'paper':
        print('It\'s a tie. Try again!')
    if computer == 'scissors':
        print("Computer wins!")
    if computer == "rock":
        print("Human wins!")

if human_input == 'scissors' or "s":
    if computer == 'scissors':
        print('It\'s a tie. Try again!')
    if computer == 'rock':
        print("Computer wins!")
    if computer == "paper":
        print("Human wins!")
