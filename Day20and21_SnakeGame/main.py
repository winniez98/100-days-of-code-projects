from turtle import Screen
import time
from snake import Snake

# create new screen
screen = Screen()
screen.setup(width=600, height=600)

# change screen's background colour
screen.bgcolor("black")

# set title of screen
screen.title("Snake Game")

# turn off tracer -> until we call update, screen won't refresh
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# TODO: Move the snake -> continuously moves forwards
game_continues = True

while game_continues:
    screen.update()
    # delay by 0.1s after all 3 segments moved
    time.sleep(0.1)

    snake.move()






# TODO: Control snake using keyboard controls


# TODO: Detect collision with food
# when it does, new piece of food randomly created on screen

# TODO: Create a scoreboard
# write text in program so once snake hits piece of food, score automatically updates

# TODO: detect collision with wall
# game should end -> Game Over
# snake stops moving

# TODO: Detect collision with tail
# game over


screen.exitonclick()
