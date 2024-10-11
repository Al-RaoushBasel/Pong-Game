from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle (r_paddle)
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x(r_paddle)
    # Detect collision with left paddle (l_paddle)
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x(l_paddle)

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset()
        score.r_point()


screen.exitonclick()
