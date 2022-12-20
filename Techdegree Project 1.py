"""
Python Web Development Tech degree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

print("Welcome to the number guessing game!")
print("pick a number between 1 and 10 ")


def start_game():
    num = random.randint(1, 10)
    attempts = 0
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess == num:
            print(f"Got it! the number was {num}, you had {attempts} attempts.")
            print("Thanks for playing :) ")
            break
        elif guess < num:
            print("It's higher ")
        else:
            print("It's lower ")


start_game()

""" Pseudo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
