# DAY 18: Turtle Graphics, Tuples, and Importing Modules

from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape()
timmy.color("blue")
timmy.speed(8)
timmy.width(5)

# DRAWING 8 DIFFERENT SIZES SHAPES
# for num_of_sides in range(3, 11):
#     new_color = (random.random(), random.random(), random.random())
#     timmy.pencolor(new_color)
#     for index in range(num_of_sides):
#         timmy.forward(60)
#         timmy.right(360 / num_of_sides)

# THE RANDOM WALK
# left_or_right = [-1, 1]
# for num_of_lines in range(200):
#     new_color = (random.random(), random.random(), random.random())
#     timmy.pencolor(new_color)
#     timmy.forward(30)
#     timmy.right(90 * random.choice(left_or_right))


# DRAWING A SPIROGRAPH
# def draw_spirograph(size_of_gap):
#     for circle in range(int(360 / size_of_gap)):
#         new_color = (random.random(), random.random(), random.random())
#         timmy.pencolor(new_color)
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size_of_gap)
#
#
# draw_spirograph(20)

screen = Screen()
screen.exitonclick()
