from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title('Pong')
screen.bgcolor('black')
screen.tracer(0)

r_paddle = Paddle()
l_paddle = Paddle()
l_paddle.setpos(-350,0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun= r_paddle.move_up, key= 'Up')
screen.onkey(fun= r_paddle.move_down, key= 'Down')
screen.onkey(fun= l_paddle.move_up, key= 'w')
screen.onkey(fun= l_paddle.move_down, key= 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.roll()

    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # collision with Right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 335:
        ball.paddle_bounce()

    # collision with Left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        ball.paddle_bounce()

    # when R Paddle misses
    if ball.xcor() > 350:
        ball.ball_reset()
        scoreboard.r_point()

    # when L Paddle misses
    if ball.xcor() < -350:
        ball.ball_reset()
        scoreboard.l_point()