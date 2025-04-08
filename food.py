from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('teal')
        self.speed('fastest')
        self.refresh()



    def refresh(self):
        random_x = randint(-260, 260)
        random_y = randint(-260, 260)
        self.goto(x=random_x, y=random_y)
