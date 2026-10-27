# Melissa Urias
# CIS256 Fall 2026
# Programming Assignment 4


import random

# List of words the computer can choose from.
words = ["python", "banana", "computer", "school", "apple"]


def select_word():
    # Choose a random word.
    return random.choice(words)


def process_guess(word, guessed_letters, guess):
    # Record the guess and check if it is in the word.
    if guess in guessed_letters:
        return False

    guessed_letters.add(guess)
    return guess in word


def display_word(word, guessed_letters):
    # Reveal all correctly guessed letters.
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )


def play_game():
    word = select_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Guess the Word!")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts remaining:", attempts)

        guess = input("Guess a letter: ").lower().strip()

        # Check that the user entered one letter.
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        if process_guess(word, guessed_letters, guess):
            print("Correct guess!")
        else:
            attempts -= 1
            print("Incorrect guess!")

        # Check whether the entire word has been guessed.
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return

    print("\nGame over! The word was:", word)


if __name__ == "__main__":
    play_game()
