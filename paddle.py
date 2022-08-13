from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.setheading(90)
        self.penup()
        self.speed("fastest")
        self.setx(x_cord)

    def go_down(self):
        if self.distance((self.xcor(), -250)) < 30:
            pass
        else:
            self.backward(40)

    def go_up(self):
        if self.distance((self.xcor(), 250)) < 30:
            pass
        else:
            self.forward(40)



