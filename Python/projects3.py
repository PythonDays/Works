# main function to start the program
def main():
    print("Welcome to my Python project!")
    
    # ask user for input
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter another number: "))
    
    # calculate the product of the two numbers
    product = num1 * num2
    
    # display the result
    print("The product of the two numbers is:", product)

# call the main function to start the program
if __name__ == "__main__":
    main()