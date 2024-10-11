from turtle import Screen
from paddle import Paddle
from ball import Ball
import random
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


ai_move_counter = 0  # Initialize a counter

def ai_move(paddle, ball):
    global ai_move_counter

    ai_move_counter += 1  # Increase the counter every frame
    if ai_move_counter % 5 != 0:  # Make the AI move every 5 frames
        return  # Skip this frame to slow down the AI

    # Move the AI paddle
    if abs(paddle.ycor() - ball.ycor()) > 20:
        if paddle.ycor() < ball.ycor():
            paddle.go_up()
        elif paddle.ycor() > ball.ycor():
            paddle.go_down()



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Let the AI move the left paddle
    ai_move(l_paddle, ball)

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x(r_paddle)
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

    # Check for game over condition (if implemented)
    if score.check_winner():
        game_is_on = False




screen.exitonclick()
