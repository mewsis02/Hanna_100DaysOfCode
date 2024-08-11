
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************                     
''')

start_game = ""

print("Welcome to The Maze!")
print("You must get to the end of the Maze without dying. Good luck!")
while start_game != "yes":
    start_game = input("\nAre you ready to play? Yes or No: ").lower()
    if start_game == "no":
        print("Please come back when you are ready to play.")
        break
    elif start_game == "yes":
        print("Game is loading now...")
        break
    else:
        print("I am sorry, but that was an invalid command!")

print("")
if start_game == "yes":
    print("You enter a room that has two doors.")
    choice1 = input("Do you take the Left (L), or the Right (R) door? ").lower()
    print("")
    if choice1 == "left" or choice1 == "l":
        print("You open the Left Door, see a long path, and start running.")
        print("When you reach the end of the path, You see a long, and deep river.")
        choice2 = input("Do you (wait) for a boat, or do you (swim) across the river? ").lower()
        print("")
        if choice2 == "wait":
            print("You decide to wait for a boat, and once you get into the boat,")
            print("You sail to the other side of the river, which has 3 more doors.")
            choice3 = input("Do you choose Red (R), Blue (B), or Yellow (Y)? ").lower()
            print("")
            if choice3 == "red" or choice3 == "r":
                print("You open the door, and get burned by the fire within. Game Over.")
            elif choice3 == "blue" or choice3 == "b":
                print("You open the door, and get attacked by 50 zombies! Game Over.")
            elif choice3 == "yellow" or choice3 == "y":
                print("You Found The Chest! You Won!")
            else:
                print("That is an invalid command. Game Over.")

        elif choice2 == "swim":
            print("You try to swim across the river, but forgot you can't swim,")
            print("so you drowned. Game Over.")
        else:
            print("That is an invalid command. Game Over.")
    elif choice1 == "right" or choice1 == "r":
        print("You open the Left Door, and see a long path, and start running,")
        print("and fall into The Abyss. Game Over.")
    else:
        print("That is an invalid command. Game Over.")
