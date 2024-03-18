from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.score_l, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score_r, align="center", font=("courier", 80, "normal"))

    def r_point(self):
        self.clear()
        self.score_l += 1

    def l_point(self):
        self.clear()
        self.score_r += 1




