from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-260,y=255)
        self.write(f'Level {self.level}', font=FONT)

    def inc_level(self):
        self.level += 1
        self.clear()
        self.write(f'Level {self.level}', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over', align='center', font=FONT)
