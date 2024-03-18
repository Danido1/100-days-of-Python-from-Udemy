from turtle import Turtle

CROSSROAD_POSITIONS = [(270, 0), (270, 10), (270, 30), (270, 50), (270, 70), (270, 90), (270, 110), (270, 130),
                       (270, 150), (270, 170), (270, 190), (270, 210), (270, 230), (270, 250), (270, 270), (290, 0)]

class CrossRoad(Turtle):
    def __init__(self):
        super(CrossRoad, self).__init__()
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=0.1)
        self.goto(0, 0)


