from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


paddle = Paddle("square", 5, 1, "white", 350)
paddle2 = Paddle("square", 5, 1, "white", -350)
ball = Ball("circle", 1, 1, "white", 0, 0)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")

screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")


is_game_on = True

def exit_game(x, y):
    global is_game_on
    is_game_on = False

screen.onscreenclick(exit_game)

while is_game_on:

    scoreboard.show_score()

    time.sleep(0.07)
    screen.update()
    ball.move()

    if ball.ycor() >= 270:
        ball.bounce(False, True)
    elif ball.ycor() <= -270:
        ball.bounce(False, True)

    if ball.distance(paddle) <= 50 or ball.distance(paddle2) <= 50:
        ball.bounce(True, True)

    # reset
    if ball.xcor() >= 370 or ball.xcor() <= -370:
        # left scores
        if ball.xcor() >= 370:
            scoreboard.update_score("left")
        elif ball.xcor() <= -370:
            scoreboard.update_score("right")

        time.sleep(1)
        screen.update()
        ball.reset()


screen.bye()
