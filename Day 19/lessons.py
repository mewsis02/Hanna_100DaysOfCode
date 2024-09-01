# DAY 19: More Turtle Graphics, Event Listeners, State, and Multiple Instances
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def turn_left():
    timmy.left(10)


def turn_right():
    timmy.right(10)


def clear():
    timmy.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.listen()
screen.exitonclick()
