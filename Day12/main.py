# Day 12 - Global and local variables
from art import logo
import random
from os import system

LIVES = {"easy": 10, "hard": 5}
NUMBER = random.randint(0, 101)


def difficulty(mode):
    return LIVES[mode]


def check_number(user_n):
    if user_n == NUMBER:
        print(f"You got it! The answer was {NUMBER}")
        return True
    elif user_n > NUMBER:
        print("Too high\nGuess again.")
        return False
    else:
        print("Too low\nGuess again.")
        return False


def guessing_game():
    system("cls")
    print(logo)
    print(
        "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100."
    )

    # print(f"Psst, the answer is: {NUMBER}")
    user_lives = difficulty(input("Choose a difficulty. Type 'easy' or 'hard': "))

    should_stop = False
    while not should_stop:
        print(f"You have {user_lives} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if check_number(user_guess) == False:
            user_lives -= 1
            if user_lives == 0:
                print("You've run out of guesses, you lose.")
                should_stop = True
        else:
            should_stop = user_guess


guessing_game()
