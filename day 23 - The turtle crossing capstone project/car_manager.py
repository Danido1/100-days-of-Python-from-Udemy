from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

STARTING_POSITIONS = [(270, 0), (270, 20), (270, 40), (270, 60), (270, 80), (270, 100), (270, 120), (270, 140),
                      (270, 160), (270, 180), (270, 200), (270, 220), (270, 240), (270, 260), (270, 280), (270, 0),
                      (270, -20), (270, -40), (270, -60), (270, -80), (270, -100), (270, -120), (270, -140),
                      (270, -160), (270, -180), (270, -200), (270, -220), (270, -240), (270, -260), (270, -280)]



class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 4)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(random.choice(STARTING_POSITIONS))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(MOVE_INCREMENT)

    def increase_level(self):
        self.car_speed += MOVE_INCREMENT
        print(f"Speed of the cars:{self.car_speed}")





