# Imports
import math
import random

# Constants
MAX_NUMBER = 30


# Functions
def is_prime(num):
  """
  Function to check if a number is prime or not.

  Args:
      num (int): Number to check

  Returns:
      bool: True if num is prime, False if not.
  """
  for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
      return False
  return True


def generate_prime_numbers(num):
  """
  Function to generate prime numbers up to a given number.

  Args:
      num (int): Maximum number to generate

  Returns:
      list: List of prime numbers
  """
  prime_numbers = []
  for i in range(2, num + 1):
    if is_prime(i):
      prime_numbers.append(i)
  return prime_numbers


def play_game():
  """
  Function to play the prime number guessing game.
  """
  print("Welcome to the Prime Number Guessing Game!")
  print("I will generate a random prime number between 2 and", MAX_NUMBER)
  print("You have to guess the number.")
  print("Let's start!")

  random_number = random.choice(generate_prime_numbers(MAX_NUMBER))
  attempts = 0
  while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess == random_number:
      print("Congratulations! You guessed the correct number in", attempts, "attempts!")
      break
    elif guess < random_number:
      print("Too low! Try again.")
    else:
      print("Too high! Try again.")


# Main function
def main():
  play_game()


# Run the main function
if __name__ == "__main__":
  main()
