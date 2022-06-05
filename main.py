# importing the choice function from the random module
import random

# Introducing the user to the Game 
print ("Welcome to the game of Rock Paper Scissors\n------------------------------------------- \n Rules of the Game \n 1. If Rock crushes Scissors \n 2. Scissors cut Paper, and \n 3. Papper covers Rock \n" )

#create a list of play options
game_list = ["R", "P", "S"]

print("Choose a option from the list below to begin \n")



#set player to False
player_move = False

while player_move == False:
#set player to True
    # Collecting user data and converting it uppercase
    player_input = input("Please select a choice from above list: ").upper()

    # setting the computer move with the choice function from the imported random module
    computer = random.choice(game_list)

    # Converting the single alhabets to the words Rock, Papper and Scissors for player_input
    if (player_input == game_list[0]):
        player_move = "Rock"
    elif (player_input == game_list[1]):
        player_move = "Paper"
    else:
        player_move = "Scissors"

    # Converting the single alhabets to the words Rock, Papper and Scissors for player_input
    if (computer == game_list[0]):
        computer_move = "Rock"
    elif (computer == game_list[1]):
        computer_move = "Paper"
    else:
        computer_move = "Scissors"

    # Printing both player and computer moves to the screen
    print ("\nPlayer " +"("+ player_move +") : "+ "Computer " + "(" + computer_move + ")")
    if player_move == computer_move:
        print("Tie!")
    elif player_move == "Rock":
        if computer_move == "Paper":
            print("You lose! ", computer_move, "covers ", player_move)
        else:
            print("You win! ", player_move, "smashes ", computer_move)
    elif player_move == "Paper":
        if computer_move == "Scissors":
            print("You lose! ", computer_move, "cut ", player_move)
        else:
            print("You win!" , player_move, "covers ", computer_move)
    elif player_move == "Scissors":
        if computer_move == "Rock":
            print("You lose...", computer_move, "smashes", player_move)
        else:
            print("You win!", player_move, "cut", computer_move)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player_move = False