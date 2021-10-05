from turtle import Turtle

ALIGNMENT = "center"
FONT = ("david", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.score_counting()

    def score_counting(self):
        self.score += 1
        self.clear()
        self.write(f"Score:  {self.score}   High Score:  {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                self.high_score = self.score
                file.write(f"{self.high_score}")
        self.score = -1
        self.score_counting()

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"Game Over \n   High Score:  {self.high_score}", align=ALIGNMENT, font=FONT)
