"""
Rock Paper Scissors Game
"""

import random

ties = 0
p_wins = 0
c_wins = 0
max_w_streak = 0
max_l_streak = 0
consec_wins = 0
consec_losses = 0

choices = {"1": "stone", "2": "paper", "3": "scissors"}

print("Enter your choice: \n 1 for Stone \n 2 for Paper \n 3 for Scissors.")

for i in range(1, 11):
    print(f"\nRound {i}")
    choice = input("Your choice (1/2/3): ")

    if choice not in choices:
        print("Invalid choice ! Please choose 1, 2, or 3.")
        continue

    p = choices[choice]
    comp = random.choice(list(choices.values()))
    
    print(f"You chose: {p}")
    print(f"Computer chose: {comp}")

    if p == comp:
        print("It's a Tie")
        ties += 1
        consec_wins = 0
        consec_losses = 0
    elif (p == "stone" and comp == "scissors") or (p == "paper" and comp == "stone") or (p == "scissors" and comp == "paper"):
        print("You win this round!")
        p_wins += 1
        consec_wins += 1
        consec_losses = 0
        if consec_wins > max_w_streak:
            max_w_streak = consec_wins
    else:
        print("Computer wins this round!")
        c_wins += 1
        consec_losses += 1
        consec_wins = 0
        if consec_losses > max_l_streak:
            max_l_streak = consec_losses

# Final results
print("\nFinal result")
print("You won:", p_wins)
print("Computer won:", c_wins)
print("Ties:", ties)
print("Your longest winning streak:", max_w_streak)
print("Your longest losing streak:", max_l_streak)

if p_wins > c_wins: 
    print("You are the Overall Winner!")
elif c_wins > p_wins:
    print("Computer is the Overall Winner!")
else:
    print("It's a Tie overall!")
