from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1,6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(300, y=randint(-240,240))
            self.all_cars.append(new_car)

    def move_left(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def inc_speed(self):
            self.car_speed += MOVE_INCREMENT


