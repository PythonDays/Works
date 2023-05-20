# Project 22
# Import necessary libraries
import random

# Define constants
MAX_NUMBER = 22

# Create a list of numbers
numbers = [i+1 for i in range(MAX_NUMBER)]

# Shuffle the list
random.shuffle(numbers)

# Print out the shuffled list
print(numbers)

# Create a loop to check for duplicates
for i in range(MAX_NUMBER):
    for j in range(i+1, MAX_NUMBER):
        if numbers[i] == numbers[j]:
            print("Duplicate found:", numbers[i])
            break