# Project 21

# Importing necessary libraries
import random


# Declaring a class for Project 21
class Project21:
  # Initializing necessary variables
  def __init__(self):
    self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

  # Function to generate a random number
  def generateRandomNumber(self):
    randomNumber = random.choice(self.numbers)
    return randomNumber

  # Function to check if the randomly generated number is divisible by 3
  def checkDivisibleBy3(self, randomNumber):
    if randomNumber % 3 == 0:
      return True
    else:
      return False

  # Function to check if the randomly generated number is divisible by 7
  def checkDivisibleBy7(self, randomNumber):
    if randomNumber % 7 == 0:
      return True
    else:
      return False

  # Function to play the game
  def playGame(self):
    print("Welcome to Project 21!")
    while True:
      input("Press enter to generate a random number...")
      randomNumber = self.generateRandomNumber()
      print("Random number: {}".format(randomNumber))
      if self.checkDivisibleBy3(randomNumber) and self.checkDivisibleBy7(randomNumber):
        print("Congratulations! You won!")
        break
      else:
        print("Better luck next time!")


# Main function
def main():
  project21 = Project21()
  project21.playGame()


# Running the main function
if __name__ == "__main__":
  main()
