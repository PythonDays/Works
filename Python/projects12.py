# import necessary libraries
import math
import random

# define variables
numbers = []

# generate 12 random numbers
for i in range(12):
    numbers.append(random.randint(0, 9))

# calculate the sum of the numbers
sum_numbers = sum(numbers)

# calculate the average of the numbers
average_numbers = sum_numbers / len(numbers)

# calculate the square root of the sum of the numbers
sqrt_sum_numbers = math.sqrt(sum_numbers)

# print the results
print("The generated numbers are: {}".format(numbers))
print("The sum of the numbers is: {}".format(sum_numbers))
print("The average of the numbers is: {}".format(average_numbers))
print("The square root of the sum of the numbers is: {}".format(sqrt_sum_numbers))
