from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# TODO: Create a screen
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
# turn tracer off
screen.tracer(0)

# TODO: Create and move a paddle

r_paddle = Paddle((350, 0))
# TODO: Create 2nd paddle
l_paddle = Paddle((-350, 0))

ball = Ball()

game_on = True

while game_on:
    # need this when tracer = off
    screen.update()
    screen.listen()
    # move right paddle
    screen.onkey(key="Up", fun=r_paddle.up)
    screen.onkey(key="Down", fun=r_paddle.down)
    # move left paddle
    screen.onkey(key="w", fun=l_paddle.up)
    screen.onkey(key="s", fun=l_paddle.down)
    # pause loop for short time during each iteration to see ball move
    time.sleep(0.1)

    ball.move()
    # TODO: Detect collision with wall and bounce
    # only need to detect collision on top and bottom wall -> on the side, it should be caught by paddles
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()




# TODO: Detect when paddle misses

# TODO: Keep score

screen.exitonclick()
