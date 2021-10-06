from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

POSITIONS = [(350, 0), (-350, 0)]

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

r_paddle = Paddle(POSITIONS[0])
l_paddle = Paddle(POSITIONS[1])
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

sleep = 0.09
game_is_on = True
while game_is_on:
    time.sleep(sleep)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320 or ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.paddle_bounce()
        sleep *= 0.9

    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.paddle_bounce()
        scoreboard.r_point()
        sleep = 0.09

    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.paddle_bounce()
        scoreboard.l_point()
        sleep = 0.09

screen.exitonclick()
