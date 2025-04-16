import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_left()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if turtle.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect when Turtle has reached the other side
    if turtle.ycor() > 280:
        turtle.level_up()
        car_manager.inc_speed()
        scoreboard.inc_level()







    screen.onkey(fun=turtle.move_up, key='Up')

screen.exitonclick()
