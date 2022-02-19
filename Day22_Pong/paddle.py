from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_len=5)
        self.setheading(90)
        self.penup()
        self.goto(x=location[0], y=location[1])

    # move paddle
    def up(self):
        self.forward(20)
        # another option: No need to set heading, stretch_wid=5, stretch_len=1
        # new_y = paddle.ycor() + 20
        # paddle.goto(paddle.xcor(), new_y)

    def down(self):
        self.backward(20)
