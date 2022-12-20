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
            print(f"Got it! the number was {num}, your attempt count is {attempts}")
            print("Thanks for playing :) ")
            break
        elif guess < num:
            print("It's higher ")
        else:
            print("It's lower ")


start_game()
