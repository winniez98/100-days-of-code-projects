import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
# turn off tracer -> get screen to update
screen.tracer(0)

turtle = Player()

# TODO: Turtle moves up when you press up key
screen.listen()
screen.onkeypress(key="Up", fun=turtle.move)

game_is_on = True
while game_is_on:
    # screen updates/code runs every 0.1 seconds
    time.sleep(0.1)
    screen.update()


screen.exitonclick()
