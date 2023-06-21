# fhwien-python-finalproject

In this repository we have two exciting projects where we use python as the programming language and use software engineering aspects.
The projects are a password generator and a hangman game.

Please enjoy our work! :")"

## Password Generator
Our passwordgenerator gives the user a secure password with defined criteria.
The criterias the user can choose from are 
- minimum length, 
- numbers and 
- special characters.

The user can write the minimum length in digits e.g. the user wants a password with at least 5 digits and can say yes or no if they want numbers or special characters in the password.
At the end the user can save the password in a specified file. We also added try-except when any errors occured while saving.

## Hangman Game
Our hangman game consists of an English-German dictionary where the word pairs are simultaneously guessed.
We decided to split our implementation into several working packages: 
- Package 1: Intro text + user name input
- Package 2: Creation of an English-German dictionary as word list (extra .py file) 
- Package 3: Hangman design with ascii (extra .py file)
- Package 4: Selection of random word pair from word list, display masked letters with underline character
 - Package 5: Guessing game with loosing lives. No life is lost when the same letter is entered again
 - Package 6: Integration and testing

To start the game, first retrieve the 4 Python files with git (in Git Bash or another UNIX shell):
```
git clone git@github.com:MelissaW88/fhwien-python-finalproject.git
```
If python is installed in your shell:
```
cd fhwien-python-finalproject/hangman
python3 hangman.py
```
Or you can open this file `hangman.py` in Thonny and execute it from there.