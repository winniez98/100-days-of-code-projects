from turtle import Screen
from paddle import Paddle

# TODO: Create a screen
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
# turn tracer off
screen.tracer(0)

# TODO: Create and move a paddle

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


game_on = True

while game_on:
    # need this when tracer = off
    screen.update()
    screen.listen()
    screen.onkey(key="Up", fun=r_paddle.up)
    screen.onkey(key="Down", fun=r_paddle.down)
    screen.onkey(key="w", fun=l_paddle.up)
    screen.onkey(key="s", fun=l_paddle.down)

# screen.update()

# TODO: Create 2nd paddle

# TODO: Create ball and make it move

# TODO: Detect collision with wall and bounce

# TODO: Detect when paddle misses

# TODO: Keep score

screen.exitonclick()
