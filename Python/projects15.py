# import relevant modules
import math
import random


# define function to calculate area of a circle
def area_circle(radius):
  area = math.pi * (radius ** 2)
  return area


# define a function to calculate the circumference of a circle
def circumference_circle(radius):
  circumference = math.pi * radius * 2
  return circumference


# define a function to generate a random number within a range
def random_number(lower_bound, upper_bound):
  random_num = random.randint(lower_bound, upper_bound)
  return random_num


# define a function to convert Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 1.8) + 32
  return fahrenheit


# main program
if __name__ == "main":
  radius = float(input("Enter the radius of the circle: "))
  print("The area of the circle is: {}".format(area_circle(radius)))
  print("The circumference of the circle is: {}".format(circumference_circle(radius)))
