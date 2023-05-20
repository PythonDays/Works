# 25 - Python Project

# Imports
import random

# Variables
numbers = []

# Functions
def generate_random_numbers():
  for i in range(25):
    numbers.append(random.randint(1,25))
  
def check_for_duplicates():
  for num in numbers:
    if numbers.count(num) > 1:
      return False
  return True

# Main
if __name__ == '__main__':
  generate_random_numbers()
  if check_for_duplicates():
    print(numbers)
  else:
    print('Duplicates found!')