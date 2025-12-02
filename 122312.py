import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

spiral = turtle.Turtle()
spiral.speed(0)
spiral.pensize(2)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta"]

length = 1

while True:
    spiral.pencolor(random.choice(colors))
    spiral.forward(length)
    spiral.right(45)
    length += 1

turtle.done()
