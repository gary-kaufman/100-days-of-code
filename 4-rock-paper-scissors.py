rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
from random import randint

print("Welcome to Rock, Paper, Scissors!\n")

players_choice_input = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")
players_choice = int(players_choice_input)
computers_choice = randint(0,2)

print("You chose...\n")
if (players_choice == 0): print(rock)
elif (players_choice == 1): print(paper)
elif (players_choice == 2): print(scissors)
print("\n")

print("The computer chose...\n")
if (computers_choice == 0): print(rock)
elif (computers_choice == 1): print(paper)
elif (computers_choice == 2): print(scissors)

# Determine outcome and print Win/Loss/Tie
if (players_choice == computers_choice):
    print("Tie!")
# First do edge cases
elif (players_choice == 0 and computers_choice == 2):
    print("You win!") # Rock beats Scissors
elif (computers_choice == 0 and players_choice == 2):
    print("You lose!") # Computer Rock beats Scissors
elif (players_choice > computers_choice):
    print("You win!") # Player Paper beats Rock or Player Scissors beats Paper
else:
    print("You lose!") # Computer Paper beats Rock or Computer Scissors beats Paper