import random

def winner(p_choice, c_choice):
    if p_choice == c_choice:
        return "It's a tie!"
    elif (p_choice == 'rock' and c_choice == 'scissors') or \
         (p_choice == 'paper' and c_choice == 'rock') or \
         (p_choice == 'scissors' and c_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

choices = ['rock', 'paper', 'scissors']

print("Welcome to Rock, Paper, Scissors!")
results = []
while True:
    p_choice = input("Enter your choice \n1 for rock\n2 for paper\n3 for scissors\n").lower()
    if p_choice == "1":
        p_choice = 'rock'
    elif p_choice == "2":
        p_choice = 'paper'
    elif p_choice == "3":
        p_choice ='scissors'
    if p_choice not in choices:
        print("Invalid choice! Please choose again.")
        continue

    c_choice = random.choice(choices)

    print("You chose:", p_choice)
    print("Computer chose:", c_choice)

    result = winner(p_choice, c_choice)
    print(result)
    
    results.append((p_choice, c_choice, result))

    play_again = input("Do you want to play again? [1 for Yes / 0 for No]: ").lower()
    if play_again != '1':
        print("Thanks for playing!")
        break

# Save results to a file
with open("game_results.txt", "w") as file:
    for result in results:
        file.write(f"Player choice: {result[0]}, Computer choice: {result[1]}, Result: {result[2]}\n")

print("Game results have been saved to 'game_results.txt'.")
