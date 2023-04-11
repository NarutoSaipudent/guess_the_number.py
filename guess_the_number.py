# Python code for Guess the Number Game
import random

def guess_the_number():
    random_number = random.randint(1, 100)
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < random_number:
            print("Too low.")
        elif guess > random_number:
            print("Too high.")
        else:
            print("Correct!")
            play_again = input("Play again? (y/n) ")
            if play_again.lower() == "y":
                guess_the_number()
            else:
                break

guess_the_number()
