
import random
import turtle
from turtle import Turtle, Screen

color_list = [(214, 157, 85), (33, 105, 151), (238, 215, 94), (153, 75, 52), (125, 168, 199), (209, 134, 163),
               (156, 60, 81), (22, 39, 54), (212, 85, 61), (176, 162, 47), (200, 85, 119), (135, 184, 150),
               (56, 119, 90), (240, 213, 4), (25, 46, 37), (228, 167, 186), (64, 46, 34), (87, 157, 100), (9, 99, 75),
               (34, 166, 189), (40, 60, 102), (228, 175, 166), (179, 189, 213), (95, 126, 173), (68, 34, 44),
               (105, 42, 60), (170, 205, 179), (113, 43, 37), (156, 206, 217), (78, 69, 35), (3, 90, 115)]

turtle.colormode(255)
timmy = Turtle()
timmy.shape()

timmy.penup()
timmy.hideturtle()
y_pos = -200
for new_line_of_circles in range(10):
    timmy.teleport(-200, y_pos)
    for circle in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
    y_pos += 50

screen = Screen()
screen.exitonclick()
