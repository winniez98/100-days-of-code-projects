# TODO: Create ball and make it move
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")

    def move(self):
        new_x = self.xcor() + 13
        new_y = self.ycor() + 10
        self.penup()
        self.speed("slowest")
        self.goto(new_x, new_y)
