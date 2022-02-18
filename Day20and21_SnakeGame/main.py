from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

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
food = Food()
scoreboard = Scoreboard()

# TODO: Control snake using keyboard controls
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_continues = True

while game_continues:

    screen.update()
    # delay by 0.1s after all 3 segments moved
    time.sleep(0.1)
    snake.move()

    # TODO: Detect collision with food
    # when it does, new piece of food randomly created on screen
    # check distance from 1st segment of snake
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # TODO: detect collision with wall
    # game should end -> Game Over
    # snake stops moving
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_continues = False
        scoreboard.game_over()

    # TODO: Detect collision with tail
    # game over
    # if head collides with any segment in tail, game over
    for square in snake.squares[1:]:
        # prevent game being automatically over because head at start is equal to head
        # if square == snake.head:
        #     pass
        # don't need above b/c slicing

        # if that's not the case, then check
        # if snake head has distance less than 10 from segment we're looping through
        if snake.head.distance(square) < 10:
            game_continues = False
            scoreboard.game_over()


screen.exitonclick()
