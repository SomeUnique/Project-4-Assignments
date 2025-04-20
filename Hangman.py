import random

def get_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer']
    return random.choice(words).lower()

def display(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = get_word()
    guessed_letters = set()
    tries = 6

    print("🎯 Welcome to Hangman!")
    print(display(word, guessed_letters))

    while tries > 0 and set(word) != guessed_letters:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that letter.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("✅ Good guess!")
        else:
            tries -= 1
            print(f"❌ Wrong guess. Tries left: {tries}")

        print(display(word, guessed_letters))

    if set(word) == guessed_letters:
        print("🎉 Congratulations! You guessed the word.")
    else:
        print(f"💀 Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
