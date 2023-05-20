# import necessary libraries
import math
import random

# Function to generate a random number between 1 and 20
def generate_number():
    return random.randint(1,20)

# Function to calculate the square root of the number
def calculate_square_root(num):
    return math.sqrt(num)

# Main program
if __name__ == '__main__':
    # Generate the random number
    num = generate_number()
    # Calculate and print the square root of the number
    square_root = calculate_square_root(num)
    print("The square root of %d is %f" % (num, square_root))