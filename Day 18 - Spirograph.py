import turtle
from turtle import Turtle, Screen
from random import randint

# object attributes
timmy = Turtle()
timmy.shape("classic")
timmy.color("teal")
timmy.speed("fastest")

turtle.colormode(255)
# selection of colors that will be picked randomly for each forward motion
def random_color():
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)
    color_bank = (r, b, g)
    return color_bank

# turtle continuously turns left, drawing a circle until completing 360 degrees, changes colors
for _ in range(36):
    timmy.circle(60)
    timmy.left(10)
    timmy.color(random_color())

# screen
screen = Screen()
screen.exitonclick()