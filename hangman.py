
import random

words = ["python", "computer", "security", "program", "internet"]

secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("===== WELCOME TO HANGMAN =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses available.")

while incorrect_guesses < max_guesses:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses, "/", max_guesses)

    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You guessed the word:", secret_word)
        break

    guess = input("Enter one letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

else:
    print("\nGame over! The word was:", secret_word)

print("Thanks for playing!")
