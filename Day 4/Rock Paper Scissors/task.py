
import random

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

choices = [rock, paper, scissors]
print("Welcome To RPS!")

player_choice = int(input("Please Choose 0 for Rock, 1 for Paper, or 2 for Scissors: "))
while player_choice > 2 or player_choice < 0:
    print("\nPlease give me a valid choice.")
    player_choice = int(input("Please Choose 0 for Rock, 1 for Paper, or 2 for Scissors: "))
player_choice = choices[player_choice]
computer_choice = choices[random.randint(0, 2)]

print(player_choice)
print("VS")
print(computer_choice)


if player_choice == computer_choice:
    print("Another Draw!")

elif player_choice == rock:
    if computer_choice == paper:
        print("You Lost!")
    if computer_choice == scissors:
        print("You Won!")

elif player_choice == paper:
    if computer_choice == rock:
        print("You Won!")
    if computer_choice == scissors:
        print("You Lost!")

elif player_choice == scissors:
    if computer_choice == rock:
        print("You Lost!")
    if computer_choice == paper:
        print("You Won!")
