from art_and_animals import HANGMANPICS
from art_and_animals import words
import random

print("Welcome to hangman!")

random_word = random.choice(words)

guessed_letters = []
display_word = ""
wrong_guesses = 0


while wrong_guesses < 6:
    print(HANGMANPICS[wrong_guesses])
    guessed_letter = input("\nGuess a letter. ")
    if guessed_letter not in guessed_letters:
        guessed_letters.append(guessed_letter)
        for letter in random_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print(display_word)
        if display_word.lower() == random_word.lower():
            print(f"\nThe word was {random_word}!")
            print("You win!")
            wrong_guesses = 100
        display_word = ""
        if guessed_letter in random_word:
            pass
        else:
            wrong_guesses += 1
            if wrong_guesses == 6:
                print(HANGMANPICS[wrong_guesses])
                print(f"\nThe word was {random_word}")
                print("Game over.")
    else:
        print("\nYou have already guessed that letter.")


