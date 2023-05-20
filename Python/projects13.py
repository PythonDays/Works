# import necessary modules
import random
import string


# create a function to generate random strings
def randomString(stringLength):
  letters = string.ascii_lowercase
  return ''.join(random.choice(letters) for i in range(stringLength))


# create a function to calculate the sum of two numbers
def sum(a, b):
  return a + b


# create a function to calculate the product of two numbers
def product(a, b):
  return a * b


# create a function to check if a number is even
def is_even(a):
  if a % 2 == 0:
    return True
  else:
    return False


# create a function to check if a number is odd
def is_odd(a):
  if a % 2 == 1:
    return True
  else:
    return
