#Imports
import math
import random
import string

#Variables
num_letters = 5

#Functions
def generate_word():
    '''Generates a random word of size num_letters'''
    letters = string.ascii_lowercase
    word = ''
    for i in range(num_letters):
        word += random.choice(letters)
    return word

def calculate_word_value(word):
    '''Calculates the value of a given word
    by summing the ordinal values of each letter'''
    total = 0
    for letter in word:
        total += ord(letter)
    return total

def main():
    '''Main logic to be executed'''
    global num_letters


print(calculate_word_value(generate_word()))
