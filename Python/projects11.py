# Declare Variables
list = []


# Define Functions
def add_number(x):
  list.append(x)


def remove_number(x):
  list.remove(x)


def print_list():
  print(list)


# Main Function
def main():
  while True:
    print("\nEnter 1 to add a number to the list")
    print("Enter 2 to remove a number from the list")
    print("Enter 3 to print the list")
    print("Enter 4 to exit")

    user_input = int(input("What would you like to do? "))

    if user_input == 1:
      number = int(input("Enter a number to add: "))
      add_number(number)

    elif user_input == 2:
      number = int(input("Enter a number to remove: "))
    try:
      remove_number(number)
    except ValueError:
      print("Number not found in the list.")


if __name__ == '__main__':
    main()
