from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
# dimensions of screen = important
screen.setup(width=500, height=400)

# popup to ask user to make bet
# this will return a string -> save to variable
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

# we want turtle to go to start of line (very left of string)
# can initialize new turtle object with shape setup -> default = arrow
y_loc = -100
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    # we're never going to pendown b/c we're moving turtle itself
    y_loc += 30
    new_turtle.goto(x=-230, y=y_loc)
    all_turtles.append(new_turtle)

# prevent while loop from starting up while user is deciding which turtle to bet on
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
