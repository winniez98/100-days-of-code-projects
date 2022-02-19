from turtle import Screen, Turtle

# TODO: Create a screen
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
# turn tracer off
screen.tracer(0)

# TODO: Create and move a paddle
# width = 20, height = 100
# x-pos = 350, y = 0
paddle = Turtle("square")
paddle.color("white")
paddle.speed("fastest")
paddle.shapesize(stretch_len=5)
paddle.setheading(90)
paddle.penup()
paddle.goto(x=350, y=0)





# move paddle
def up():
    paddle.forward(20)


def down():
    paddle.backward(20)


game_on = True

while game_on:
    # need this when tracer = off
    screen.update()
    screen.listen()
    screen.onkey(key="Up", fun=up)
    screen.onkey(key="Down", fun=down)

# screen.update()

# TODO: Create 2nd paddle

# TODO: Create ball and make it move

# TODO: Detect collision with wall and bounce

# TODO: Detect when paddle misses

# TODO: Keep score

screen.exitonclick()
