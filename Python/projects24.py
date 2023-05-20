# define project 24
def project_24():
    
    # create a list of numbers
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    
    # create an empty list
    result = []
    
    # loop through the numbers list
    for num in numbers:
        
        # check if the number is divisible by 3
        if num % 3 == 0:
            result.append(num)
        
    # display the result
    print(result)

# call the function
project_24()