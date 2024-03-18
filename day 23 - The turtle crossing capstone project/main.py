import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from crossroad import CrossRoad

screen = Screen()
screen.bgcolor("grey")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
crossroad = CrossRoad()

screen.onkeypress(fun=player.up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Car collision with turtle
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    # Detect when the turtle has reached the top edge
    if player.ycor() > 280:
        player.goto(0, -280)
        scoreboard.level_up()
        car_manager.increase_level()

screen.exitonclick()




