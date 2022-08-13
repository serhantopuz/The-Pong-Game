from turtle import Turtle


class Score(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.goto(x_cor, 230)
        self.write(f"{self.score}", False, "center", ("Arial", 50, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", False, "center", ("Arial", 50, "normal"))
