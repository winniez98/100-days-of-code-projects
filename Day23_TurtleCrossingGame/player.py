from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.finish_line = FINISH_LINE_Y
        # TODO: Create turtle that starts at bottom of the screen
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.go_to_start()

    def go_to_start(self):
        self.goto(STARTING_POSITION[0], STARTING_POSITION[1])

    # TODO: Turtle moves up when you press "up" key
    def move(self):
        self.forward(MOVE_DISTANCE)

    # another option:
    # def is_at_finish_line(self):
    #     if self.ycor() > FINISH_LINE_Y:
    #         return True
    #     else:
    #         return False





