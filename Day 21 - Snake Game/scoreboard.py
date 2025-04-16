from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('courier', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
                with open('data.txt') as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.color('white')
        self.goto(x= 0, y= 270)
        self.write(f'Score: {self.score} High Score: {self.highscore}', align= ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.highscore}', align= ALIGNMENT, font=FONT)

    def game_over(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode="w") as file:
                file.write(f'{self.highscore}')
        self.score = 0
        self.update_scoreboard()

    def scoring(self):
        self.score += 1
        self.update_scoreboard()
