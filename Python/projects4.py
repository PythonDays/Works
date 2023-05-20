# Import necessary libraries
import math
import time

# Define the function to calculate the area of a circle
def calculate_area(radius):
    return math.pi * radius**2

# Define the function to calculate the circumference of a circle
def calculate_circumference(radius):
    return 2 * math.pi * radius

# Define the main function
def main():
    # Ask the user for a radius
    radius = float(input('Enter radius: '))

    # Calculate the area and circumference
    area = calculate_area(radius)
    circumference = calculate_circumference(radius)

    # Print the results
    print("Area of circle is", area)
    print("Circumference of circle is", circumference)

# Execute the program
if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time)
