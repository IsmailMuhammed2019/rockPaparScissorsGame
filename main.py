# importing choice function from random module
import random

# Setting the game_list
game_list = ("R", "P", "S")

# welcoming player and printing out the rules of the game
print("Welcome to the game of Rock, Paper, Scissors \n----------------------------------------------\n Rules Of The Game \n 1. Rock beats Scissors \n 2. Paper beats Rock  \n 3. Scissors beats Paper \n \nPlease enter a choice from the list below  \n'R' for Rock, \n'P' for Paper, and \n'S' for Scissors")


# setting a while loop to check if the user input is in the list if not end the game
while True:
    player_input = input("\nPlease enter your choice from the list above: ")

    # converting the inputs to uppercase
    player_choice = player_input.upper()

    # Setting the user input to the words Rock, Paper, Scissors.
    def settingplayerValue(player_value):
        if (player_choice == game_list[0]):
            player_value = "Rock"
        elif (player_choice == game_list[1]):
            player_value = "Paper"
        elif (player_choice == game_list[2]):
            player_value = "Scissors"
        return player_value

    

    # Getting the computer choice
    computer_choice = random.choice(game_list)

    # Setting the computer random choice to the words Rock paper, scissors
    def settingcomputerValue(computer_value):
        if (computer_choice == game_list[0]):
            computer_value = "Rock"
        elif (computer_choice == game_list[1]):
            computer_value = "Paper"
        elif (computer_choice == game_list[2]):
            computer_value = "Scissors"
        return computer_value 
    
    player = settingplayerValue(player_choice)
    computer = settingcomputerValue(computer_choice)

    # Setting an if condition to check 
    if (player_choice in game_list):
        # Printing the choosen value on the screen
        print("\nPlayer (" + player + ")" + " : " + "Computer (" + computer + ")")
        # while loop to check if the game is a tie it should replay
        player == 'rock' and computer == 'paper'
        print('Computer wins, paper covers rock')
        break
    elif player == 'rock' and computer == 'scissors':
        print('You win, rock smashes scissors')
        break
    elif player == 'paper' and computer == 'rock':
        print('You win, paper covers rock')
        break
    elif player == 'paper' and computer == 'scissors':
        print('Computer wins, scissors cut paper')
        break
    elif player == 'scissors' and computer == 'rock':
        print('Computer wins, rock smashes scissors')
        break
    elif player == 'scissors' and computer == 'paper':
        print('You win, scissors cut paper') 
        break
    elif player == computer:
        print('The game is a tie, Replay') 

    else:
        print("\nPlease Re-enter a valid choice from the above choices")