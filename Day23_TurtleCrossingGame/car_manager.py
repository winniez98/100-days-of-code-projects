from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# starting move distance
STARTING_MOVE_DISTANCE = 5
# how much move increases every time user levels up
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.add_car()

    def add_car(self):
        # TODO: Create cars that are 20px high and 40px wide: randomly generated along y-axis and move across screen
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        rand_y = random.randint(-250, 250)
        new_car.goto(320, rand_y)
        self.cars.append(new_car)

    def move(self):
        for i in range(len(self.cars) - 1):
            x_cor = self.cars[i].xcor() - STARTING_MOVE_DISTANCE
            self.cars[i].goto(x_cor, self.cars[i].ycor())
