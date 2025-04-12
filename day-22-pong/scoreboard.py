from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.left_score = 0
        self.right_score = 0

    def show_score(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        score = f"{self.left_score} : {self.right_score}"
        font_style = ("Arial", 16, "normal")
        self.write(score, align="center", font=font_style)

    def update_score(self, side):
        if side is "left":
            self.left_score += 1
        elif side is "right":
            self.right_score += 1

