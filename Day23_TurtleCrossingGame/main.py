import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
# turn off tracer -> get screen to update
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# TODO: Turtle moves up when you press up key
screen.listen()
screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
i = 0
while game_is_on:
    # screen updates/code runs every 0.1 seconds
    time.sleep(0.1)
    screen.update()

    # TODO: Generate a car every 6th time the game loop runs
    i += 1
    if i % 6 == 0:
        car_manager.add_car()

    car_manager.move()

    # TODO: Detect collision with a car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # TODO: Detect when player has reached edge of the screen
    # another option
    # if player.is_at_finish_line():
    if player.ycor() > player.finish_line:
        car_manager.increase_speed()
        player.go_to_start()
        scoreboard.increase_level()


screen.exitonclick()
