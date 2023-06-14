#importing all necessary modules 
import random
import sys

#creating the function for the project 
def project3():
    #declaring the variables
    number_list = []
    number_count = 0
    total_sum = 0
    #asking the user to enter the numbers
    while number_count < 3:
        number = int(input("Enter number: "))
        number_list.append(number)
        number_count += 1
    print("\nYou entered: ", number_list)
    #calculating the total sum of the numbers 
    for numbers in number_list:
        total_sum += numbers
    print("\nThe total sum is: ", total_sum)
    #displaying the result
    if total_sum < 0:
        print("\nThe result is negative")
    elif total_sum > 0:
        print("\nThe result is positive")
    else:
        print("\nThe result is 0")
    #asking the user if they want to continue
    while True:
        answer = input("\nDo you want to continue (Y/N): ").lower()
        if answer == 'y':
            project3()
            break
        elif answer == 'n':
            print("\nBye! Thank you for using this program.")
            sys.exit()
        else:
            print("\nPlease enter a valid option.")

#calling the function
project3()