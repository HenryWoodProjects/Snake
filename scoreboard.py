from turtle import Turtle

ALIGNMENT = "center"
FONT = "Courier"
FORMAT = (FONT, 16, "bold")
LARGE_FORMAT = (FONT, 24, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.update()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update()

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write(f"GAME OVER", False, ALIGNMENT, LARGE_FORMAT)
        self.color("white")
        if self.score > self.high_score:
            self.high_score = self.score
        self.goto(0, -30)
        self.write(f"Final Score: {self.score}", False, ALIGNMENT, LARGE_FORMAT)

    def update(self):
        self.write(f"Score: {self.score}", False, ALIGNMENT, FORMAT)
