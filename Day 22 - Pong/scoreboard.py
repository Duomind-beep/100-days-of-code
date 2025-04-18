from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('courier', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.update_board()

    def update_board(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100,200)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.update_board()

    def r_point(self):
        self.r_score += 1
        self.update_board()

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align= ALIGNMENT, font=FONT)