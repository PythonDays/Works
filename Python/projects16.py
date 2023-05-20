# Import necessary libraries
import math
import random


# Define a function to generate a random number
def get_random_number():
  return random.randint(1, 16)


# Define a function to check whether a number is prime
def is_prime(num):
  if num < 2:
    return False
  elif num == 2:
    return True
  else:
    for i in range(2, int(math.sqrt(num)) + 1):
      if num % i == 0:
        return False
    return True


# Main program
while True:
  # Generate a random number
  rand_num = get_random_number()

  # Check whether this number is a prime
  if is_prime(rand_num):
    print(f'The number {rand_num} is a prime number!')
    break
