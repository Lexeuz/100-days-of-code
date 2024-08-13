from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.r_player = 0
        self.l_player = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.l_player, align="center", font=("Courier", 50, "bold"))
        self.goto(100, 230)
        self.write(self.r_player, align="center", font=("Courier", 50, "bold"))

    def l_point(self):
        self.l_player += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_player += 1
        self.update_scoreboard()
