from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()

screen.listen()
# move right paddle
# onkeypress to make sure you can hold down key and keep paddle moving
screen.onkeypress(key="Up", fun=r_paddle.up)
screen.onkeypress(key="Down", fun=r_paddle.down)
# move left paddle
screen.onkeypress(key="w", fun=l_paddle.up)
screen.onkeypress(key="s", fun=l_paddle.down)

game_on = True

while game_on:
    # need this when tracer = off
    screen.update()

    # pause loop for short time during each iteration to see ball move
    time.sleep(ball.move_speed)

    ball.move()
    # TODO: Detect collision with wall and bounce
    # only need to detect collision on top and bottom wall -> on the side, it should be caught by paddles
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO: Detect collision with paddle
    # normally use distance method to check distance with wall and paddle
    # if less than certain amount, can be sure they hit
    # ball.distance(paddle) < 20 -> probably made contact
    # but what if ball doesn't hit paddle in the centre?
    # distance measures from centre of ball to centre of paddle -> won't register as collision
    # add additional condition: if ball went past certain point on x axis AND its within 50 px distance from paddle
    # then probably made contact with paddle

    # detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # TODO: Detect when paddle misses
    # detect right paddle miss
    if ball.distance(r_paddle) > 50 and ball.xcor() > 380:
        ball.reset_ball()
        ball.bounce_x()
        scoreboard.l_point()

    # detect left paddle miss
    if ball.distance(l_paddle) > 50 and ball.xcor() < -380:
        ball.reset_ball()
        ball.bounce_x()
        scoreboard.r_point()

screen.exitonclick()
