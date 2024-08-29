
# DAY 16 : Object-Oriented Programming

# from turtle import Turtle, Screen
#
# little_tim = Turtle()
# print(little_tim)
# little_tim.shape("turtle")
# little_tim.color("LightPink1")
# little_tim.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()

# Creates a new PrettyTable
from prettytable import PrettyTable
table = PrettyTable()

pokemon_names = ["Pikachu", "Squirtle", "Charmander"]
pokemon_types = ["Electric", "Water", "Fire"]

# Adds 2 columns, named Pokémon Name and Type, to the PrettyTable
table.add_column("Pokemon Name", pokemon_names)
table.add_column("Type", pokemon_types)

# Aligns all the columns in our table to be (left, right, or center) aligned
table.align = "l"

print(table)
