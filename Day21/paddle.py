from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.create_paddle(position=pos)

    def create_paddle(self, position):
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
