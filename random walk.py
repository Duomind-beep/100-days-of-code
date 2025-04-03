from turtle import Turtle, Screen
from random import choice, randint

# object attributes
timmy = Turtle()
timmy.shape("classic")
timmy.color("teal")
timmy.pensize(20)
timmy.speed(10)

# selection of colors that will be picked randomly for each forward motion
color_bank = ["royal blue", "pale violet red", "sea green", "light sky blue", "dark orange"]

# randomizes turning function
def turning():
    turn = randint(0,1)
    print(turn)
    if turn == 0:
        timmy.right(90)
    else:
        timmy.left(90)


# random walk loop
for _ in range(100):
    paces = randint(1, 90)
    timmy.forward(paces)
    turning()
    timmy.color(choice(color_bank))




# screen
screen = Screen()
screen.exitonclick()