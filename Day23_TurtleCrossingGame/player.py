from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.finish_line = FINISH_LINE_Y
        self.create_turtle()

    def create_turtle(self):
        # TODO: Create turtle that starts at bottom of the screen
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION[0], STARTING_POSITION[1])


    # TODO: Turtle moves up when you press "up" key
    def move(self):
        self.forward(MOVE_DISTANCE)




