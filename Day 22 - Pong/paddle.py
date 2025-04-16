from turtle import Turtle

PADDLE_LENGTH = 5
UP = 90
DOWN = 270
PACES = 40

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(UP)
        self.speed('fastest')
        self.shapesize(stretch_len=PADDLE_LENGTH)
        self.shape('square')
        self.setpos(x=350, y=0)
        self.color('white')

    def move_up(self):
        self.forward(PACES)

    def move_down(self):
        self.backward(PACES)
