from turtle import Turtle

FONT_ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_count = 0
        self.arg = "Score : " + str(self.score_count)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(self.arg, move=False, align=FONT_ALIGN, font=FONT)
        self.hideturtle()

    def score(self):
        self.score_count += 1
        self.arg = "Score : " + str(self.score_count)
        self.clear()
        self.write(self.arg, move=False, align=FONT_ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.arg = "***GAME OVER***"
        FONT_ALIGN = "center"
        self.write(self.arg, move=False, align=FONT_ALIGN, font=FONT)

