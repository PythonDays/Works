# import necessary modules
import math
import random

# create an empty list
my_list = []

# loop 10 times
for i in range(10):
    # generate a random number between 1 and 10
    num = random.randint(1, 10)
    # add the number to the list
    my_list.append(num)

# calculate the average of the list
average = sum(my_list) / len(my_list)

# calculate the standard deviation of the list
n = len(my_list)
std_dev = math.sqrt(sum([(x - average)**2 for x in my_list]) / n)

# print out the list and the standard deviation
print("List:", my_list)
print("Standard Deviation:", std_dev)
