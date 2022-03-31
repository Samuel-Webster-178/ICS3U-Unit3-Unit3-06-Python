#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program allows user to guess number


import random


def main():
    # I check if the user guessed correctly
    chosen_number = random.randint(0, 9)

    # input
    guess = int(input("Guess a number between 0-9: "))

    # process&output
    if chosen_number == guess:
        print("You got it!")
    else:
        print("Maybe next time!")

    print("\nDone.")


if __name__ == "__main__":
    main()
