import turtle
from dot_painting_utils import turn_left, turn_right, run

turtle.colormode(255)

# These are the Object attributes
damien = turtle.Turtle()
damien.shape('classic')
damien.color('teal')
damien.penup()
damien.speed('fast')
damien.hideturtle()

# Moves the turtle to the starting position
damien.goto(-300,-250)

# This is the dot drawing loop
for _ in range(3):
    run(damien)
    turn_left(damien)
    run(damien)
    turn_right(damien)

# Screen attributes
screen = turtle.Screen()
screen.exitonclick()
