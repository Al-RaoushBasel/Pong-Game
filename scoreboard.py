from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 190)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 190)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def check_winner(self):
        if self.l_score >= 10:
            self.goto(0, 0)
            self.write("Left Player Wins!", align="center", font=("Courier", 40, "normal"))
            return True
        elif self.r_score >= 10:
            self.goto(0, 0)
            self.write("Right Player Wins!", align="center", font=("Courier", 40, "normal"))
            return True
        return False

