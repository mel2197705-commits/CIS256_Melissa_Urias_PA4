
# Melissa Urias
# CIS256 Fall 2026
# Programming Assignment 4

from guess_the_word import (
    words,
    select_word,
    process_guess,
    display_word,
)


def test_select_word():
    # Check that the random word is in the word list.
    word = select_word()
    assert word in words


def test_correct_guess():
    # Check that a correct guess returns True.
    guessed_letters = set()
    result = process_guess("python", guessed_letters, "p")

    assert result is True
    assert "p" in guessed_letters


def test_incorrect_guess():
    # Check that an incorrect guess returns False.
    guessed_letters = set()
    result = process_guess("python", guessed_letters, "z")

    assert result is False
    assert "z" in guessed_letters


def test_repeated_letters():
    # Check that repeated letters are all revealed.
    guessed_letters = {"a"}
    result = display_word("banana", guessed_letters)

    assert result == "_ a _ a _ a"


def test_display_word():
    # Check that letters not guessed remain hidden.
    guessed_letters = {"p", "t"}
    result = display_word("python", guessed_letters)

    assert result == "p _ t _ _ _"


def test_duplicate_guess():
    # Check that duplicate guesses are recognized.
    guessed_letters = {"p"}
    result = process_guess("python", guessed_letters, "p")

    assert result is False
    assert guessed_letters == {"p"}

def test_letters_any_order():
    # Verify correct letters can be guessed in any order.
    guessed_letters = set()

    process_guess("apple", guessed_letters, "e")
    process_guess("apple", guessed_letters, "a")
    process_guess("apple", guessed_letters, "p")

    assert display_word("apple", guessed_letters) == "a p p _ e"
    
