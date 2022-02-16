# W = forwards
# S = backwards
# A = counterclockwise (left)
# D = clockwise (right)
# C = clear drawing and turtle back in centre

from turtle import Turtle, Screen

sketch = Turtle()
screen = Screen()

screen.listen()


# functions
def move_forwards():
    sketch.forward(10)


def move_backwards():
    sketch.backward(10)


def move_left():
    new_heading = sketch.heading() + 10
    sketch.setheading(new_heading)


def move_right():
    new_heading = sketch.heading() - 10
    sketch.setheading(new_heading)


def clear_screen():
    screen.resetscreen()


screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
