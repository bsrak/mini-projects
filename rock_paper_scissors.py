import random

user_wins = 0
computer_wins = 0
draws = 0

options = ["rock","paper","scissors"]

while True:
    user_choice = input("Type Rock\Paper\Scissors or press Q to quit: ").lower()
    if user_choice == "q":
        break

    if user_choice not in options:
        continue
    random_number = random.randint(0,2)
    # rock:0, paper:1, scissors:2
    computer_choice = options[random_number]
    print("Computer picked", computer_choice + ".")

    if user_choice == "rock" and computer_choice == "scissors":
        print("You won!")
        user_wins += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You won!")
        user_wins += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You won!")
        user_wins += 1
    elif user_choice == computer_choice:
        print("Draw!")
        draws += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print(draws, "draws.")
print("Goodbye!")
