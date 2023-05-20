# import libraries
import random

# create a list with numbers from 1 to 27
numbers = list(range(1, 28))

# shuffle the list
random.shuffle(numbers)

# print out the list
print(numbers)

# create a variable to store the sum
sum = 0

# use a for loop to add up the list elements
for number in numbers:
    sum += number

# print out the sum
print("The sum of the numbers is:", sum)