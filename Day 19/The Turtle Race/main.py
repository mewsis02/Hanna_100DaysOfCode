from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
user_bet = user_bet.lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = [0, 0, 0, 0, 0, 0]

for turtle_index in range(0, 6):
    turtles[turtle_index] = Turtle(shape="turtle")
    turtles[turtle_index].color(colors[turtle_index])
    turtles[turtle_index].penup()
    turtles[turtle_index].goto(x=-230, y=-80 + (40 * turtle_index))

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
