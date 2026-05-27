import random

words = ["python", "coding", "hangman", "laptop", "github"]
word = random.choice(words)
guessed = []
lives = 6

while lives > 0:
    display = [letter if letter in guessed else "_" for letter in word]
    print(" ".join(display))

    if "_" not in display:
        print("You won!")
        break

    guess = input("Guess a letter: ").lower()
    if guess in guessed:
        print("Already guessed!")
    elif guess in word:
        guessed.append(guess)
        print("Correct!")
    else:
        guessed.append(guess)
        lives -= 1
        print(f"Wrong! Lives left: {lives}")
else:
    print(f"You lost! Word was: {word}")