# import necessary modules 
import random 

# define list of possible answers 
answers = ["yes", "no", "maybe", "try again"]

# define main function 
def main(): 
    # get user question 
    question = input("What is your question?\n") 
    
    # generate a random answer 
    answer = random.choice(answers) 
    print(answer) 
    
# call main function 
main()