from turtle import Turtle, Screen
from random import choice

timmy = Turtle()
timmy.shape("classic")
timmy.color("teal")




color_bank = ["royal blue", "pale violet red", "sea green", "light sky blue", "dark orange"]


num_sides = 2
for _ in range(10):
    num_sides += 1
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(360 / num_sides)
        timmy.color(choice(color_bank))




screen = Screen()
# screen.screensize(5000,5000)
screen.exitonclick()