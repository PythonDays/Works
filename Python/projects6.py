import random

# Create a list of words
words = ["supercalifragilisticexpialidocious", "onomatopoeia", "antidisestablishmentarianism",
         "floccinaucinihilipilification", "sesquipedalian", "quizzical", "hackneyed", "jocose",
         "accoutrement", "leitmotif"]


# Function to choose random word from list
def choose_word():
    return random.choice(words)


# Function to check if the word has been used already
def check_word(word):
    if word in words:
        return True
    else:
        return False


# Function to print the word
def print_word(word):
    for char in word:
        print(char, end=" ")
    print("\n")


# Function to guess word
def guess_word(word, guessed_letters):
    for char in word:
        if char in guessed_letters:
            print(char, end=" ")
        else:
            print("_", end=" ")
    print("\n")


# Function to check if the guessed letter is in the word
def is_letter_in_word(letter, word):
    if letter in word:
        return True
    else:
        return False


# Function to play the game
def play_game():
    word = choose_word()
    guessed_letters = []
    attempts = 0

    print("Welcome to the Word Guessing Game!")
    print("Try to guess the word.")

    while True:
        print_word(word)
        guess = input("Enter a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            attempts += 1

            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")

            elif is_letter_in_word(guess, word):
                guessed_letters.append(guess)

                if len(guessed_letters) == len(set(word)):
                    print_word(word)
                    print("Congratulations! You guessed the word in", attempts, "attempts!")
                    break

            else:
                print("Wrong guess. Try again.")

        else:
            print("Invalid input. Try again.")


# Main function
def main():
    play_game()


# Run the main function
if __name__ == "__main__":
    main()
