# TODO: Create a scoreboard
# write text in program so once snake hits piece of food, score automatically updates

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Calibri", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):

        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        # scoreboard = turtle which knows how to keep track of score and how to display in program

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
