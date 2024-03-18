from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        with open("data.txt", "r") as d:
            self.high_level = int(d.read())
        self.penup()
        self.goto(-60, 250)
        self.hideturtle()
        self.write(f"Level: {self.level} Highest level: {self.high_level}", align="center", font=("Courier", 24, "normal"))

    def level_up(self):
        self.level += 1
        if self.level > self.high_level:
            self.high_level = self.level
            with open("data.txt", "w") as d:
                d.write(f"{self.high_level}")
        self.clear()
        self.write(f"Level {self.level} Highest level: {self.high_level}", align="center", font=("Courier", 24, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))


