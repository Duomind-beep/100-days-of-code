import colorgram
import turtle
from random import choice


# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 6)

color_bank = []

for extract in colors:
    rgb = extract.rgb
    color_bank.append(rgb)

'''Randomly selects a color for the next dot'''
def color_switch():
    paint = choice(color_bank)
    return paint

'''the forward walk & dot function'''
def walking(turtle_obj):
    color_switch()
    turtle_obj.dot(50,color_switch())
    turtle_obj.forward(100)

'''turn left function'''
def turn_left(turtle_obj):
    turtle_obj.left(90)
    walking(turtle_obj)
    turtle_obj.left(90)

'''turn right function'''
def turn_right(turtle_obj):
    turtle_obj.right(90)
    walking(turtle_obj)
    turtle_obj.right(90)

'''prints 6 dots at a time'''
def run(turtle_obj):
    for _ in range(6):
        walking(turtle_obj)
