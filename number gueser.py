import random
n=int(input("Enter a number range:"))
num_guess = random.randint(1, n+1)
attempts = 0

print("Welcome to the Number Guesser Game!")
print(f"I have selected a number between 1 and {n}. Can you guess it?")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < num_guess:
        print("Guess Higher! Try again.")
    elif guess > num_guess:
        print("Guess Lower! Try again.")
    else:
        print(f"Congratulations! You guessed the number {num_guess} correctly in {attempts} attempts.")
        break
