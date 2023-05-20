#import modules 
import math 
import time 

#initialize variables
start_time = time.time()
number = 9

#calculate factorial of number 
factorial = math.factorial(number)

#print results
print("The factorial of {} is {}".format(number, factorial))

#calculate total time
total_time = time.time() - start_time

#print total time
print("Total time taken: {:.2f} seconds".format(total_time))