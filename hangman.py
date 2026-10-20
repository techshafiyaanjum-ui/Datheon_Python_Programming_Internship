import random

# Words taken from the provided word list
words = [
    "python",
    "computer",
    "database",
    "keyboard",
    "network",
    "developer",
    "internet",
    "school",
    "technology",
    "system"
]

word = random.choice(words)

guessed_letters = []
attempts = 6

print("===== HANGMAN GAME =====")

while attempts > 0:

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord :", display)
    print("Attempts Left :", attempts)

    if "_" not in display:
        print("\nCongratulations! You Won 🎉")
        break

    guess = input("Enter a Letter: ").lower()

    if len(guess) != 1:
        print("Enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess ✅")
    else:
        print("Wrong Guess ❌")
        attempts -= 1

if attempts == 0:
    print("\nGame Over 💀")
    print("Correct Word was:", word)

print("\nThank You For Playing!")