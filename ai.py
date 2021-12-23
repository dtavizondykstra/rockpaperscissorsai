from random import randint

print("\nWelcome to the Rock, Paper, Scissors Terminal Game! \n ")
print("Player 1, make your move:")

player_1_choice = input().lower()

# computer is the Computer
print("\nComputer, make your move:")
rand_num = randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(computer)


print("\nAND THE WINNER IS...")

# Tie =======================================================================
if player_1_choice == computer:
    print("Tie!")
# Rock =======================================================================
elif player_1_choice == "rock":
    if computer == "paper":
        print("Computer!")
    elif computer == "scissors":
        print("Player 1!")
# Scissors =====================================================================
elif player_1_choice == "scissors":
    if computer == "rock":
        print("Computer!")
    elif computer == "paper":
        print("Player 1!")
# Paper =======================================================================
elif player_1_choice == "paper":
    if computer == "scissors":
        print("Computer!")
    elif computer == "rock":
        print("Player 1!")
# Else =======================================================================
else:
    print("Error, please enter a valid move")
