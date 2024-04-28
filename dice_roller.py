import random

print("Welcome to the Dice Rolling Simulator!")

while True:
    input("Press Enter to roll the dice...")
    value = random.randint(1, 6)
    print("You rolled:", value)
    
    again = input("Do you want to roll again? [1 for Yes / 0 for No]: ").lower()
    if again != '1':
        print("Thanks for playing!")
        break