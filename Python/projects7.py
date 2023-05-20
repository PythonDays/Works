# import modules
import random
import math


# define functions
def generate_random_number():
  return random.randint(1, 10)


def calculate_distance(x1, y1, x2, y2):
  return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# define variables
x1 = 0
y1 = 0

# main program
running = True
while running:
  x2 = generate_random_number()
  y2 = generate_random_number()

  print("The distance between ({0}, {1}) and ({2}, {3}) is {4}".format(
    x1, y1, x2, y2, calculate_distance(x1, y1, x2, y2)
  ))

  response = input("Press 'q to quit or any other key to continue: ")
  if response.lower() == 'q':
    running = False

  print("Program ended.")
