from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# Setup screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

# Initialize paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

# Ask the user to choose the game mode: AI or Two-Player
game_mode = screen.textinput("Choose Game Mode", "Type '1' for AI mode or '2' for Two Player mode:")

# Function to handle AI movement for AI Mode
def ai_move(paddle, ball):
    if abs(paddle.ycor() - ball.ycor()) > 20:
        if paddle.ycor() < ball.ycor():
            paddle.go_up()
        elif paddle.ycor() > ball.ycor():
            paddle.go_down()

# Main game loop after mode selection
def start_game():
    screen.listen()

    # Player 2 control for Two Player Mode
    if game_mode == '2':
        screen.onkey(l_paddle.go_up, "w")
        screen.onkey(l_paddle.go_down, "s")

    # Player 1 control (always present)
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")

    # Main game loop
    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # AI Mode: Let AI control the left paddle
        if game_mode == '1':
            ai_move(l_paddle, ball)

        # Detect collision with walls
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

        # Check for game over (if implemented)
        if score.check_winner():
            game_is_on = False

# Start the game after the mode is chosen
start_game()

screen.exitonclick()
