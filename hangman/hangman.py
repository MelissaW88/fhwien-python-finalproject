# Hangman game to improve English and/or German vocabulary.

import random
from hangman_ascii import print_hangman
from hangman_intro import print_intro

# Import dictionary from an additional python file.
from hangman_dic_en_de import english_german_dictionary

# Select random English word with its German translation.
chosen_word_pair = random.choice(list(english_german_dictionary.items()))

# Calculate lengths of words.
word_length = len(chosen_word_pair)


def get_random_word():
    return random.choice(list(english_german_dictionary.items()))


# Display masked letters with underline symbol.
def print_word(word, guessed_letters):
    return " ".join(
        [letter if letter.lower() in guessed_letters else "_" for letter in word]
    )


# Developping hangman guessing game with loosing lives. The player has 6 lives in total.
def play_hangman():
    word, translation = get_random_word()

    guessed_letters = set()
    lives = 6

    print_intro()
    print(
        "The English word has {} and the German word {} letters.".format(
            len(word), len(translation)
        )
    )
    print()

    print_hangman(lives)

    while lives > 0:
        print(f"Lives left: {lives}")
        print("English: ", print_word(word, guessed_letters))
        print("German: ", print_word(translation, guessed_letters))
        print()

        # Letters can be entered in lower or upper cases.
        guess = input("Enter a letter: ").lower()

        # No life is lost when the same letter is entered again.
        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess not in word.lower() and guess not in translation.lower():
            print("Wrong guess.")
            lives -= 1
            print_hangman(lives)

        if all(letter in guessed_letters for letter in word) and all(
            letter.lower() in guessed_letters for letter in translation
        ):
            print(
                f"Congratulations! You guessed the English word {word} "
                f"and its German translation {translation}"
            )
            return

    print(
        "Sorry, you lost. The English word was",
        word,
        "and its German translation was",
        translation,
    )


play_hangman()
