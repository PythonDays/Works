# Import necessary modules
import random
import time

# Initialize some variables
total_score = 0

# Start the game
print("Let's play a game!")

# Loop through the game 10 times
for i in range(10):
    # Generate a random number between 1 and 10
    random_number = random.randint(1, 10)

    # Get the user's guess
    user_guess = int(input("Guess a number between 1 and 10: "))

    # Check to see if the user's guess is correct
    if user_guess == random_number:
        total_score += 1
        print("You guessed correctly! You get a point!")
    else:
        print("Sorry, that was not correct. The correct number was", random_number)

    # Wait for 1 second
    time.sleep(1)