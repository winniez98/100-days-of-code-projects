# TODO: Create a scoreboard
# write text in program so once snake hits piece of food, score automatically updates

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Calibri", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # for high score
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        # couldn't clear hear previously b/c we wanted score to still be there when game was over
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_score()
        # scoreboard = turtle which knows how to keep track of score and how to display in program

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    # instead of stopping game, reset scoreboard
    def reset(self):
        # if current score > high score, update higher score
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))

        # once we update highscore, reset score
        self.score = 0

        # update scoreboard
        self.update_score()
