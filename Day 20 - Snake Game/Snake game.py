
# Create food for the snake and make her bigger each time, and one the snake ate the food create another piece of food
# randomly in the screen.
# Create a scoreboard
# Game ends when snake collision with screen or his own tail

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Create the playground
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("El juego de la serpiente")
screen.tracer(0)
# Control de snake with keybindings.
snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()



# Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

# Detect collision with wall
    if snake.head.xcor() > 305 or snake.head.xcor() < -305 or snake.head.ycor() > 305 or snake.head.ycor() < -305:
        scoreboard.reset()
        snake.reset()


# Detect collision with tail
    for part in snake.snake_parts[1:]:
        if snake.head.distance(part) < 10:
            scoreboard.reset()
            snake.reset()




screen.exitonclick()
