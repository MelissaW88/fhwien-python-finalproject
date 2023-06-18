# Introduction and Asking the name of player

import time  # To use some delays for dramatic effect

rules = "You have to guess an English word and its German translation. To guess the words, you have to enter one letter each try. If the word contains this letter, it gets displayed. If the words doesn't contain this letter, you loose a life. You have 6 lives in total."


def print_intro():
    print("-----------------------------------------")
    print(
        "              - Hangman - "
        + "\n"
        + "Guess the word and its German translation"
    )
    print("-----------------------------------------")

    time.sleep(1)

    print("\n" + "What's your name?")
    # Asking for the name of the player to use later during the game as a nice touch
    name = input()

    time.sleep(1)

    print("Hello " + name + ". Do you know the rules of the game?")

    knowsrules = input()

    if (
        knowsrules == "no"
        or knowsrules == "No"
        or knowsrules == "n"
        or knowsrules == "N"
    ):
        print(rules + "\n")
        time.sleep(2)

    print("Let's start!")
