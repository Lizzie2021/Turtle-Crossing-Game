from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setx(300)
        new_car.setheading(180)
        new_car.color(random.choice(COLORS))
        new_car.sety(random.randint(-250, 250))
        self.all_cars.append(new_car)

    def move_cars(self, level):
        speed = STARTING_MOVE_DISTANCE + (level - 1) * MOVE_INCREMENT
        for car in self.all_cars:
            car.forward(speed)

