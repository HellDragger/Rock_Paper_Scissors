import random
import time  # Time module for sleep function
from collections import Counter  # Counter to count the number in a data structure
# Number of times you wish to play
n = int(input("How many times do you wish to play?: "))
# List that includes rock paper scissors
rock_paper_scissors = ["Scissors", "Paper", "Rock"]

win_list = []   # list to store results of all plays
for i in range(0, n):
    # the computer chooses randomly from the list(or string) using choice function
    computer_choice = random.choice(rock_paper_scissors)
    # choices given to user
    print("Choices:-\n1. Rock\n2. Paper\n3. Scissors")
    # The number input is recorded
    user_number = int(input("Enter your choice: "))
    # number converted to its respective choice
    if user_number == 1:
        user_choice = "Rock"
    elif user_number == 2:
        user_choice = "Paper"
    else:
        user_choice = "Scissors"

    print("You chose:- ", user_choice)
    print("Computer chose:- ", computer_choice)
    # for different choices of user and computer
    if user_choice != computer_choice:
        if user_choice == "Rock":
            if computer_choice == "Scissors":
                win_list.append("Won")
                print("You Won!!!!")
            else:
                win_list.append("Lost")
                print("You Lost!!!!")
        elif user_choice == "Paper":
            if computer_choice == "Rock":
                win_list.append("Won")
                print("You Won!!!!")
            else:
                win_list.append("Lost")
                print("You Lost!!!!")
        else:
            if computer_choice == "Paper":
                win_list.append("Won")
                print("You Won!!!!")
            else:
                win_list.append("Lost")
                print("You Lost!!!!")
    # for same choices of user and computer
    else:
        win_list.append("Draw")
        print("Draw!!!!")
    time.sleep(5) # Delay in execution
#     do you wish to change condition to be added

# counter to count number of wins, loses and draw respectively

print("The results are: ", Counter(win_list))
