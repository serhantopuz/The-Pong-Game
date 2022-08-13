from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()

def draw_dashed_line():
    dashed_line = Turtle("square")
    dashed_line.sety(280)
    dashed_line.color("white")
    dashed_line.setheading(270)
    dashed_line.hideturtle()
    for i in range(14):
        dashed_line.forward(25)
        dashed_line.penup()
        dashed_line.forward(15)
        dashed_line.pendown()
def screen_settings(screen):
    screen.title("The Pong Game")
    screen.setup(width=1000, height=600)
    screen.bgcolor("black")
    screen.listen()
    screen.tracer(0)


screen_settings(screen)
draw_dashed_line()

r_paddle = Paddle(450)
l_paddle = Paddle(-450)
ball = Ball()
r_score = Score(50)
l_score = Score(-50)


screen.onkey(l_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "Up")


is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 420 or ball.distance(l_paddle) < 50 and ball.xcor() < -420:
        ball.bounce_x()

    if ball.xcor() > 480:
        ball.reset_ball()
        l_score.update_score()

    if ball.xcor() < -480:
        ball.reset_ball()
        r_score.update_score()





screen.exitonclick()



