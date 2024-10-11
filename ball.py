from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.07

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Method for bouncing off top and bottom walls (vertical direction)
    def bounce_y(self):
        self.y_move *= -1  # Reverse the Y direction

    # Method for bouncing off paddles (horizontal direction)
    def bounce_x(self, paddle):
        difference = self.ycor() - paddle.ycor()
        self.y_move = difference / 10  # Adjust the ball's angle based on hit position
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.06
        self.x_move *= -1
