# NiceHexSpiral.py
import turtle
from turtle import Screen

screen = Screen()

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('white')
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(59)

screen.exitonclick()