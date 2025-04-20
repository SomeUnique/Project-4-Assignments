import random

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")

# Computer selects a random number
secret_number = random.randint(1, 100)
attempts = 0

# Game loop
while True:
    guess = input("Take a guess: ")

    # Check if the input is a number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You guessed the number in {attempts} tries.")
        break
