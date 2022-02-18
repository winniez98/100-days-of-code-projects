from turtle import Turtle
import random


# piece of food on screen = turtle object
class Food(Turtle):
    def __init__(self):
        # instead of self.food = Turtle(), want it to inherit from Turtle
        super().__init__()

        # can now use things from turtle class
        self.shape("circle")
        self.penup()  # doesn't draw

        # stretch turtle along length and width(normally 20x20)
        # stretch width by halving it
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    # food goes to new random location
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
