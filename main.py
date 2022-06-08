# importing choice function from random module
import random

# Setting the game_list
game_list = ("R", "P", "S")

# welcoming player and printing out the rules of the game
print("Welcome to the game of Rock, Paper, Scissors \n----------------------------------------------\n Rules Of The Game \n 1. Rock beats Scissors \n 2. Paper beats Rock  \n 3. Scissors beats Paper \n \nPlease enter a choice from the list below  \n'R' for Rock, \n'P' for Paper, and \n'S' for Scissors")


# setting a while loop to check if the user input is in the list if not end the game
while True:
    player_input = input("\nplease enter your choice from the list above: ")

    # converting the inputs to uppercase
    player_choice = player_input.upper()

    if (player_choice in game_list):
        print('You can play the game')
    else:
        print("Please Re-enter a valid choice from the above choices")