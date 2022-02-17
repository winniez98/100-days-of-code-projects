from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # code here determines what happens when we initialize new snake objet
        # TODO: Create a snake body
        # made up of 3 squares lined up next to each other
        # use self when working in class
        self.squares = []
        self.create_snake()

        # head of snake -> b/c we use it multiple times
        self.head = self.squares[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_square = Turtle(shape="square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(position)
            self.squares.append(new_square)

    def move(self):
        for square_num in range(len(self.squares) - 1, 0, -1):
            # get position of 2nd last square
            # loop through segments going from last to first (reverse order) -> use range
            # start at length of snake(squares) , stop at 0, and step of -1
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            # tell last square to go to position of 2nd last square
            self.squares[square_num].goto(new_x, new_y)
            # move first segment
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # snake can't turn back on itself -> if facing down, then can't go up
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
