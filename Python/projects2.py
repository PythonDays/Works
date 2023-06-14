#import modules
import os
import sys

#define functions
def welcome():
    print("Welcome to this python project!")
    
def menu():
    print("Please choose an option from the menu:")
    print("1. Print File")
    print("2. Rename File")
    print("3. Exit")

def printFile():
    filename = input("Please enter the name of the file you wish to print: ")
    try:
        with open(filename) as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("Sorry, the file was not found.")
    
def renameFile():
    oldName = input("Please enter the name of the file you wish to rename: ")
    newName = input("Please enter the new name for the file: ")
    os.rename(oldName, newName)
    print("The file has been renamed successfully.")

#main program
welcome()

while True:
    menu()
    option = input()
    if option == "1":
        printFile()
    elif option == "2":
        renameFile()
    elif option == "3":
        sys.exit()
    else:
        print("Invalid option. Please try again.")