import random

def display_intro():
    print("Welcome to Hangman!")
    print("*************************")
    name = input("Enter your name: ")
    print(f"Hello, {name}! Let's play hangman.")

def create_word_list():
    word_list = {
        "apple": "Apfel",
        "banana": "Banane",
        "cat": "Katze",
        "dog": "Hund",
        "elephant": "Elefant",
        # Add more word pairs as needed
    }
    return word_list

def display_hangman(lives):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |
           |
           |
           -
        ''',
        '''
           --------
           |      |
           |
           |
           |
           |
           -
        ''',
        '''
           --------
           |      |
           |
           |
           |
           |
           |
        '''
    ]
    print(stages[lives])

def mask_word(word):
    return "_" * len(word)

def display_word(word):
    print(" ".join(word))

def update_word(word, letter, english_word):
    new_word = list(word)
    for i, char in enumerate(english_word):
        if char == letter:
            new_word[i] = letter
    return "".join(new_word)

def play_game():
    word_list = create_word_list()
    english_word, german_word = random.choice(list(word_list.items()))
    masked_word = mask_word(english_word)
    guessed_letters = []
    lives = 7

    while lives > 0:
        print(f"\nWord: {masked_word}")
        print(f"Guesses: {', '.join(guessed_letters)}")
        display_hangman(lives)

        letter = input("Guess a letter: ").lower()

        if letter in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.append(letter)

        if letter in english_word:
            masked_word = update_word(masked_word, letter, english_word)
            if masked_word == english_word:
                print(f"\nCongratulations! You guessed the word: {english_word}")
                break
        else:
            print("Incorrect guess.")
            lives -= 1

    if lives == 0:
        print(f"\nGame over! The word was: {english_word}")

    print(f"The German translation is: {german_word}")

def main():
    display_intro()
    play_game()

if __name__ == '__main__':
    main()
