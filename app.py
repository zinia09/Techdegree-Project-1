import random

print("Welcome to the number guessing game!")
print("pick a number between 1 and 10 ")


def start_game():
    num = random.randint(1, 10)
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess == num:
                print(f"Got it! the number was {num}, you had {attempts} attempts.")
                print("Thanks for playing :) ")
                break
            elif guess not in range(1, 11):
                print('Choose a number between 1 and 10')
            elif guess < num:
                print("It's higher ")
            elif guess > num:
                print("It's lower ")
        except:
            print("enter a value between 1 and 10")


start_game()
