# Hangman Design


def print_hangman(lives):
    if lives == 6:
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")

    elif lives == 5:
        print("\n+---+")
        print(" O  |")
        print("    |")
        print("    |")
        print("   ===")

    elif lives == 4:
        print("\n+---+")
        print(" O  |")
        print(" |  |")
        print("    |")
        print("   ===")

    elif lives == 3:
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")

    elif lives == 2:
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")

    elif lives == 1:
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")

    elif lives == 0:
        print("\n+---+")
        print(" X  |")
        print("/|\ |")
        print("/ \ |")
        print("   ===")
