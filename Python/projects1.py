#Importing necessary libraries
import time
import random

#Defining the function
def run_game():
    print("Welcome to the game!")
    time.sleep(2)

    #Creating a list of possible choices
    choices = ["rock", "paper", "scissors"]

    #Initializing the score
    player_score = 0
    computer_score = 0

    #Game loop
    while (player_score < 3 and computer_score < 3):
        #Prompting the player for a choice
        player_choice = input("Choose rock, paper or scissors: ")
        
        #Validating the choice
        if player_choice not in choices:
            print("Invalid choice, please try again.")
            continue
        
        #Generating a random choice for the computer
        computer_choice = random.choice(choices)
        print("Computer chose: " + computer_choice)

        #Determining the winner
        if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            player_score += 1
        elif (player_choice == computer_choice):
            print("Draw!")
        else:
            print("Computer wins!")
            computer_score += 1
        print("Current score is: Player: " + str(player_score) + " Computer: " + str(computer_score))
        time.sleep(2)

    #Determining the grand winner
    if player_score == 3:
        print("You won the game!")
    else:
        print("Computer won the game!")

#Calling the function
run_game()