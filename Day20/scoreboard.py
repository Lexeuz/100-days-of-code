from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 17, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as record:
            self.high_score = int(record.read())
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    # Files, directories and paths.
    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as record:
                record.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}  High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
